#!/usr/bin/env sh

set -e

case "$1" in
    app)
        alembic -c backend/alembic.ini upgrade head || echo "Миграции завершились с ошибкой..."

        exec python -m backend.app
        ;;
    *)
        exec "$@"
esac