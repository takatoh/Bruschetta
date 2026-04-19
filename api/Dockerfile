FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get upgrade -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
  && pip install poetry \
  && pip install poetry-plugin-export

RUN groupadd -g 1000 bruschetta \
  && useradd -u 1000 -g bruschetta -m -s /bin/bash bruschetta

USER bruschetta
WORKDIR /app

RUN poetry config virtualenvs.in-project true
#RUN poetry install

ENV PYTHONPATH=/app
ENV LANG=ja_JP.UTF-8

CMD ["./start.sh"]
