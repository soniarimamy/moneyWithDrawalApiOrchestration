from datetime import timedelta
from temporalio import workflow
from schemas.common_schemas import CustomHttpRequestError
from schemas.account_schemas import IMoneyWithDrawalValidation, IUserAccountVerification


@workflow.defn
class MoneyWithDrawalWorkflow:
    @workflow.run
    async def run(self, money_with_draw_validation: IMoneyWithDrawalValidation | CustomHttpRequestError):
        user_account_verification = IUserAccountVerification(
            account_number=money_with_draw_validation.account_number,
            account_password=money_with_draw_validation.account_password
        )
        check_account_balance_resp = await workflow.execute_activity(
            "check_account_balance", user_account_verification, start_to_close_timeout=timedelta(10)
        )
        if 'error' not in check_account_balance_resp:
            validate_money_withdrawal_resp = await workflow.execute_activity(
                "validate_money_withdrawal", money_with_draw_validation, start_to_close_timeout=timedelta(10)
            )
            return validate_money_withdrawal_resp
        else:
            return check_account_balance_resp
