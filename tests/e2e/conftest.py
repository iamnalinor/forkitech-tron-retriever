import os
from pathlib import Path

import pytest
from starlette.testclient import TestClient

# ROOT_DIR is a directory where `tests` dir is located
ROOT_DIR = Path(__file__).parent.parent.parent
os.chdir(ROOT_DIR)


@pytest.fixture()
def client() -> TestClient:
    from api.misc import app

    return TestClient(app)
