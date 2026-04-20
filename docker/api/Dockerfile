FROM debian:trixie AS builder

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y git
RUN git clone https://github.com/takatoh/bruschetta.git


FROM python:3.13.13-slim-trixie

RUN apt-get update && apt-get upgrade -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
  && pip install poetry \
  && poetry config virtualenvs.in-project true

ENV PYTHONPATH=/app
ENV LANG=ja_JP.UTF8

WORKDIR /app

COPY --from=builder /bruschetta/api/ ./
RUN poetry install
COPY files/bruschetta.conf ./instance

EXPOSE 5000

CMD [ "./start.sh" ]
