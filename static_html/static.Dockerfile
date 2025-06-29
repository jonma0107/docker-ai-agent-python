FROM python:3.13.4-slim-bullseye

WORKDIR /app

COPY ./src /app

CMD ["python", "-m", "http.server", "8000"]