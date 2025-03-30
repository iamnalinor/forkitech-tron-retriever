from typing import Annotated

from pydantic import StringConstraints

from api.schemas.base import BaseSchema


class WalletRequestModel(BaseSchema):
    wallet_address: Annotated[str, StringConstraints(pattern=r"T[A-Za-z1-9]{33}")]


class WalletResponseModel(BaseSchema):
    bandwidth: float
    energy: float
    trx_balance: float
