from typing import Annotated

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.deps.database import SessionDep
from api.models import Request


class RequestRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def log_request(self, wallet_address: str) -> Request:
        request = Request(wallet_address=wallet_address)
        self.session.add(request)
        await self.session.commit()
        return request

    async def get_requests(self, offset: int = 0, limit: int = 10) -> list[Request]:
        result = await self.session.execute(
            select(Request)
            .order_by(Request.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(result.scalars())


def get_request_repository(db: SessionDep) -> RequestRepo:
    return RequestRepo(db)


RequestRepoDep = Annotated[RequestRepo, Depends(get_request_repository)]
