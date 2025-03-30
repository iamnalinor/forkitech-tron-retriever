from typing import Annotated

from annotated_types import Ge
from fastapi import APIRouter

from api.repository import RequestRepoDep
from api.schemas import LoggedRequestModel

request_router = APIRouter(tags=["Requests"])


@request_router.get("/requests", description="Get logged requests in descending order")
async def get_requests(
    request_repo: RequestRepoDep,
    offset: Annotated[int, Ge(0)] = 0,
    limit: Annotated[int, Ge(0)] = 10,
) -> list[LoggedRequestModel]:
    return [
        LoggedRequestModel.model_validate(request)
        for request in await request_repo.get_requests(offset, limit)
    ]
