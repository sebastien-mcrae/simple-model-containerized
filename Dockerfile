FROM python:3.11-slim

ARG UID=10000
ARG GID=10000

ARG POETRY_VERSION=1.6.1

USER root

WORKDIR /opt/app/

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y bash \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -g "${GID}" mygroup \
    && useradd -m -u "${UID}" -g mygroup myuser \
    && chown -R myuser:mygroup /opt/app/ \
    && chmod -R 755 /opt/app/

USER myuser

COPY --chown=myuser . .

ENV PATH="/home/myuser/.local/bin:${PATH}"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN curl -sSL https://install.python-poetry.org | python3 - --version "${POETRY_VERSION}"

RUN poetry install --only main

ENTRYPOINT ["./entrypoint.sh"]
