from typing import Annotated

from annotated_types import Ge
from fastapi import APIRouter
from starlette.responses import JSONResponse

from api.repository import RequestRepoDep
from api.schemas import LoggedRequestModel

ping_router = APIRouter(tags=["Ping"])


@ping_router.get("/ping", description="Healthcheck")
async def ping() -> dict[str, str]:
    return {"status": "ok"}
