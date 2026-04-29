#!/usr/bin/env bash
set -e

BACKEND="$(cd "$(dirname "$0")" && pwd)"
VENV="$BACKEND/.venv"

# ── 1. Зависимости ────────────────────────────────────────────────
echo ">>> Установка зависимостей..."
python3 -m venv "$VENV"
source "$VENV/bin/activate"
pip install --quiet --upgrade pip
pip install --quiet -r "$BACKEND/requirements.txt"

# ── 2. Миграции ───────────────────────────────────────────────────
echo ">>> Миграция базы данных..."
python "$BACKEND/manage.py" migrate --noinput

# ── 3. Статика ────────────────────────────────────────────────────
echo ">>> Сборка статических файлов..."
python "$BACKEND/manage.py" collectstatic --noinput

echo ">>> Build завершён."
