FROM python:3.12.4

WORKDIR /app

ENV FLASK_APP run.py

COPY requirements.txt .
COPY .env .env

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT python3 run_dev.py