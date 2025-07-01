FROM python:3.13.4-slim-bullseye

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Instala streamlit si no está en requirements.txt
RUN pip install --no-cache-dir streamlit

COPY ./src /app/src

EXPOSE 8501

CMD ["streamlit", "run", "src/streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]