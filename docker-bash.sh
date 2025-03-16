#!/usr/bin/env sh

set -e

case "$1" in
    app)
        # Выполняем миграции, используя конфигурацию из backend/alembic.ini, без смены директории
        alembic -c backend/alembic.ini upgrade head || echo "Миграции завершились с ошибкой..."
        # Запускаем приложение, оставаясь в рабочей директории /opt/app
        exec python -m backend.app
        ;;
    *)
        exec "$@"
esac