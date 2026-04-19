FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get upgrade -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
  && pip install poetry \
  && pip install poetry-plugin-export \
  && poetry config virtualenvs.in-project true

WORKDIR /app

ENV PYTHONPATH=/app
ENV LANG=ja_JP.UTF-8

CMD ["./start.sh"]
