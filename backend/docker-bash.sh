#!/usr/bin/env sh

set -e

case "$1" in
    app)
        alembic upgrade head && exec python app.py
        ;;
    *)
        exec "$@"
esac