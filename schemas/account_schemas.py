from pydantic import BaseModel


class IUserAccountVerification(BaseModel):
    account_number: str
    account_password: int


class OUserAccountVerification(BaseModel):
    currency: str
    account_balance: float


class IMoneyWithDrawalValidation(IUserAccountVerification):
    money_to_withdraw: float


class OMoneyWithDrawalValidation(BaseModel):
    money_to_withdraw: float
    last_account_balance: float
    actual_account_balance: float
    currency: str
