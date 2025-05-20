import httpx
from temporalio import activity
from helpers.constants import global_variables
from schemas.common_schemas import CustomHttpRequestError
from schemas.account_schemas import IMoneyWithDrawalValidation, IUserAccountVerification


@activity.defn
async def check_account_balance(user_account_verification: IUserAccountVerification):
    async with httpx.AsyncClient() as client:
        check_account_balance_api = f"{global_variables['MONEY_WITHDRAWAL_API']}/check-balance"
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        check_account_balance_api_response = await client.post(
            url=check_account_balance_api, headers=headers, json=user_account_verification.dict()
        )
        return check_account_balance_api_response.json()


@activity.defn
async def validate_money_withdrawal(money_with_draw_validation: IMoneyWithDrawalValidation | CustomHttpRequestError):
    async with httpx.AsyncClient() as client:
        money_with_draw_validation_api = f"{global_variables['MONEY_WITHDRAWAL_API']}/validate-withdrawal"
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        money_with_draw_validation_api_response = await client.post(
            url=money_with_draw_validation_api, headers=headers, json=money_with_draw_validation.dict()
        )
        return money_with_draw_validation_api_response.json()
