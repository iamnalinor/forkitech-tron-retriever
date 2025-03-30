run:
	alembic upgrade head
	python -m uvicorn api.misc:app

up:
	docker compose up -d --build

export:
	uv export --no-dev > requirements.txt
	uv export --only-dev > requirements-dev.txt

lint:
	ruff check --fix
	ruff format

test:
	pytest

.PHONY: run up export lint test