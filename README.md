# forkitech-tron-retriever

Микросервис для получения информации о кошельках Tron с логированием всех запросов в БД.

## Настройка

1. Зарегистрируйтесь на https://www.trongrid.io/ и получите API-ключ
2. Скопируйте `.env.dist` в `.env` и вставьте полученный ключ в переменную `TRONPY_HTTP_API_KEY`

## Запуск

### Вручную

1. `pip install -r requirements.txt -r requirements-dev.txt`
2. `alembic upgrade head`
3. `uvicorn api.misc:app`

### Docker

```bash
docker compose up -d
```

Приложение будет запущено на http://127.0.0.1:8000/. Swagger-спецификация будет доступна по http://127.0.0.1:8000/docs.

### Тесты

```bash
pytest
```
