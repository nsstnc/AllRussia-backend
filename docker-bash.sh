#!/usr/bin/env sh

set -e

case "$1" in
    app)
        # Переходим в папку backend для выполнения миграций
        cd backend
        # Здесь alembic ищет файл alembic.ini и папку миграций относительно папки backend
        alembic upgrade head || echo "Миграции завершились с ошибкой..."
        # Возвращаемся в рабочую директорию
        cd ..
        # Запускаем приложение как пакет – так Python корректно находит модуль backend
        exec python -m backend.app
        ;;
    *)
        exec "$@"
esac