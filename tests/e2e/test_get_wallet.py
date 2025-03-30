import time
from http import HTTPStatus

from starlette.testclient import TestClient

NON_EXISTING_WALLET = "TL9eFCZKsL4s1M8gPiwq2MJdkuKvtWZoV8"
BINANCE_COLD_WALLET = "TNPdqto8HiuMzoG7Vv9wyyYhWzCojLeHAF"
BINANCE_BANDWIDTH = 100_000
BINANCE_ENERGY = 1_000_000_000


def test_invalid_wallet(client: TestClient) -> None:
    response = client.post("/wallet", json={"walletAddress": "invalid address"})
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_unknown_wallet(client: TestClient) -> None:
    resp = client.post("/wallet", json={"walletAddress": NON_EXISTING_WALLET})
    assert resp.status_code == HTTPStatus.NOT_FOUND

    time.sleep(1)

    resp = client.get("/requests")
    assert resp.json()[0]["walletAddress"] == NON_EXISTING_WALLET


def test_known_wallet(client: TestClient) -> None:
    resp = client.post("/wallet", json={"walletAddress": BINANCE_COLD_WALLET})
    assert resp.status_code == HTTPStatus.OK
    data = resp.json()
    assert data["bandwidth"] > BINANCE_BANDWIDTH
    assert data["energy"] > BINANCE_ENERGY
    assert data["trxBalance"] > 0

    time.sleep(1)

    resp = client.get("/requests")
    assert resp.json()[0]["walletAddress"] == BINANCE_COLD_WALLET
    assert resp.json()[1]["walletAddress"] == NON_EXISTING_WALLET
