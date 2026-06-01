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

RUN groupadd -g 1000 bruschetta \
  && useradd -u 1000 -g bruschetta -m -s /bin/bash bruschetta

ENV PYTHONPATH=/app
ENV LANG=ja_JP.UTF8

USER bruschetta
WORKDIR /app

COPY --from=builder --chown=1000:1000 /bruschetta/api/ ./
RUN pip install --user -r requirements.txt \
  && pip install --user gunicorn

EXPOSE 5000

CMD [ "/home/bruschetta/.local/bin/gunicorn", "--bind", "0.0.0.0:5000", "bruschetta:create_app()" ]
