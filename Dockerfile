FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG API_KEY
ENV API_KEY=${API_KEY}

EXPOSE 8081

CMD echo "CMC_API_KEY=${API_KEY}" > .env && uvicorn src.main:app --host 0.0.0.0 --port 8081