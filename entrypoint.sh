set -e
alembic upgrade head
uvicorn api.misc:app --host 0.0.0.0 --port 8000