#!/usr/bin/env sh

set -e

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-5000}
WORKERS=${WORKERS:-1}

poetry run flask run --host "$HOST"
