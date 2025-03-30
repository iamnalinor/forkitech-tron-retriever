from fastapi import FastAPI

from api import handlers

app = FastAPI()
app.include_router(handlers.ping_router)
app.include_router(handlers.request_router)
app.include_router(handlers.wallet_router)
