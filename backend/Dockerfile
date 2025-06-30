FROM python:3.13.4-slim-bullseye

RUN apt-get update && apt-get install -y curl
# curl -X POST -d  '{"message": "Hello, FASTAPI!"}' -H "Content-Type: application/json" http://localhost:8000/api/chat/
# curl -X POST -d  '{"message": "Hello, FASTAPI!"}' -H "Content-Type: application/json" https://docker-ai-agent-python-production-0067.up.railway.app/api/chat/
# curl http://localhost:8000/api/chat/recent/
# curl https://docker-ai-agent-python-production-0067.up.railway.app/api/chat/recent/


# Create python virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src /app
