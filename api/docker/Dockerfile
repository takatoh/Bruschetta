FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get upgrade -y \
  && pip install --upgrade pip \
  && pip install poetry \
  && poetry config virtualenvs.in-project true \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV PYTHONPATH=/app
ENV LANG=ja_JP.UTF-8

CMD ["./start.sh"]
