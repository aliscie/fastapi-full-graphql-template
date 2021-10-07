FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
#for psycopg2
RUN apt-get update && apt-get clean all && rm -rf /var/lib/apt/lists/*

#for requests
RUN apt-get install libpq-dev

RUN python3 -m pip install pipenv
RUN python3 -m pipenv install --deploy --system
EXPOSE 8000