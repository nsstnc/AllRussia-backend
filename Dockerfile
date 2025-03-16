FROM python:3.10.5-slim-buster as base
LABEL maintainer="allrussia-python"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /opt/app


FROM base
COPY requirements.txt ./
RUN echo "deb http://archive.debian.org/debian buster main" > /etc/apt/sources.list && \
    echo "deb-src http://archive.debian.org/debian buster main" >> /etc/apt/sources.list
RUN apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y --no-install-recommends \
    git libpq-dev python3-dev build-essential libsnappy-dev dos2unix && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN pip install -r requirements.txt
COPY . .
RUN dos2unix docker-bash.sh && chmod +x docker-bash.sh
ENTRYPOINT ["/opt/app/docker-bash.sh"]

EXPOSE 5000