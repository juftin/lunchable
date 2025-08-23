ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y jq && apt-get clean

# configure uv
ENV UV_LINK_MODE=copy \
    UV_LOCKED=1 \
    UV_COMPILE_BYTECODE=1
# Install dependencies
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-install-project --no-dev

COPY README.md /app/README.md
COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock
COPY lunchable /app/lunchable

# Install project
RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --no-dev --extra plugins

ENV PATH="/app/.venv/bin:${PATH}"

SHELL ["/bin/bash", "-c"]

RUN _LUNCHABLE_COMPLETE=bash_source lunchable > ${HOME}/.lunchable-complete.bash && \
    echo "[[ ! -f ${HOME}/.lunchable-complete.bash ]] || source ${HOME}/.lunchable-complete.bash" >> /root/.bashrc

CMD ["lunchable", "--help"]
