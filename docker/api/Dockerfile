FROM debian:trixie AS builder

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y git
RUN git clone https://github.com/takatoh/bruschetta.git


FROM python:3.13.13-slim-trixie

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

ENV PYTHONPATH=/app
ENV LANG=ja_JP.UTF8

WORKDIR /app

COPY --from=builder /bruschetta/api/ ./
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "/usr/local/bin/flask", "run", "--host=0.0.0.0", "--port=5000" ]
