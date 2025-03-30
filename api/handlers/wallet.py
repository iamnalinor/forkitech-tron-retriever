import asyncio

from fastapi import APIRouter
from starlette.exceptions import HTTPException
from tronpy import AsyncTron
from tronpy.exceptions import AddressNotFound, BadAddress
from tronpy.providers import AsyncHTTPProvider

from api.config import TRONPY_HTTP_API_KEY, TRONPY_HTTP_PROVIDER_URI
from api.repository import RequestRepoDep
from api.schemas import WalletRequestModel, WalletResponseModel

wallet_router = APIRouter(tags=["Wallet"])

background_tasks = set[asyncio.Task]()


@wallet_router.post("/wallet", description="Get info about wallet")
async def get_wallet(
    request_repo: RequestRepoDep, request: WalletRequestModel
) -> WalletResponseModel:
    # Log request in background
    task = asyncio.ensure_future(request_repo.log_request(request.wallet_address))

    # Store reference for a task. See asyncio-dangling-task
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)

    async with AsyncTron(
        AsyncHTTPProvider(
            endpoint_uri=TRONPY_HTTP_PROVIDER_URI,
            api_key=TRONPY_HTTP_API_KEY,
        )
    ) as client:
        try:
            balance = await client.get_account_balance(request.wallet_address)
            res = await client.get_account_resource(request.wallet_address)
            bandwidth = (
                res["freeNetLimit"]
                - res.get("freeNetUsed", 0)
                + res.get("NetLimit", 0)
                - res.get("NetUsed", 0)
            )
            energy = res.get("EnergyLimit", 0) - res.get("EnergyUsed", 0)
        except (BadAddress, AddressNotFound):
            raise HTTPException(404, "Wallet not found") from None

    return WalletResponseModel(
        bandwidth=bandwidth,
        energy=energy,
        trx_balance=balance,
    )
