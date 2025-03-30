from unittest.mock import AsyncMock, Mock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from api.repository.request import RequestRepo


@pytest.mark.asyncio
async def test_request_repo_add() -> None:
    db = AsyncSession()
    db.add = Mock()
    db.commit = AsyncMock()

    repo = RequestRepo(db)
    result = await repo.log_request("mock-wallet-address")
    assert result.wallet_address == "mock-wallet-address"

    db.add.assert_called_once_with(result)
    db.commit.assert_called_once()
