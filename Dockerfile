FROM ghcr.io/astral-sh/uv:python3.12-alpine
WORKDIR /opt
STOPSIGNAL SIGKILL
EXPOSE 8000
ENV UV_PROJECT_ENVIRONMENT=/usr/local

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync --frozen --no-dev

COPY . .

RUN dos2unix entrypoint.sh
CMD ["/bin/sh", "entrypoint.sh"]
HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=5 \
    CMD wget -q -O - http://localhost:8000/ping || exit 1
