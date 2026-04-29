#!/usr/bin/env bash
set -e

BACKEND="$(cd "$(dirname "$0")" && pwd)"
VENV="$BACKEND/.venv"

source "$VENV/bin/activate"

HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"

exec gunicorn backend.wsgi:application \
    --chdir "$BACKEND" \
    --bind "$HOST:$PORT" \
    --workers 1 \
    --access-logfile - \
    --error-logfile -
