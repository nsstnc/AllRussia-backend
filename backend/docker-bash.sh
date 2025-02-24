#!/usr/bin/env sh

set -e

case "$1" in
    app)
        # Попытка применения миграций, но ошибки не останавливают выполнение
        alembic upgrade head || echo "Миграции завершились с ошибкой, продолжаем запуск"
        exec python app.py
        ;;
    *)
        exec "$@"
esac