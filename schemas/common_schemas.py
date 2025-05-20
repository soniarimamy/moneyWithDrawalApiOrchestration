from pydantic import BaseModel


class CustomHttpRequestError(BaseModel):
    error: str
    message: str
    status: str
