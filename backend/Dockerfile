FROM python:3.10.5-slim-buster as base
LABEL maintainer="allrussia-python"

ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /opt/backend
ENTRYPOINT ["./docker-bash.sh"]
FROM base
COPY requirements.txt ./
# Используем архивные репозитории
RUN echo "deb http://archive.debian.org/debian buster main" > /etc/apt/sources.list && \
    echo "deb-src http://archive.debian.org/debian buster main" >> /etc/apt/sources.list

# Отключаем проверку срока действия репозиториев и устанавливаем зависимости
RUN apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y --no-install-recommends \
    git libpq-dev python3-dev build-essential libsnappy-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install -r requirements.txt
COPY ./* ./
EXPOSE 5000