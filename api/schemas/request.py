import datetime

from api.schemas.base import BaseSchema


class LoggedRequestModel(BaseSchema):
    id: int
    created_at: datetime.datetime
    wallet_address: str
