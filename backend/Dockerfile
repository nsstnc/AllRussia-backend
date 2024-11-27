FROM python:3.10.5-slim-buster as base
LABEL maintainer="allrussia-python"
# This flag is important to output python logs correctly in docker!
ENV PYTHONUNBUFFERED 1
# Flag to optimize container size a bit by removing runtime python cache
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /opt/backend
ENTRYPOINT ["./docker-bash.sh"]
FROM base
COPY requirements.txt ./
RUN echo "deb http://archive.debian.org/debian/ buster main" > /etc/apt/sources.list
RUN echo "deb-src http://archive.debian.org/debian/ buster main" >> /etc/apt/sources.list

RUN apt-get install debian-archive-keyring
RUN apt-get update
RUN apt-get -y install libpq-dev && apt-get install -y build-essential
RUN pip install -r requirements.txt
COPY ./* ./
EXPOSE 5000
