FROM python:3.13-slim

LABEL authors="marius.ciurea"

ENV PYTHONPATH=/app

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 3333

CMD ["uvicorn", "src.services:app", "--host", "0.0.0.0", "port", "3333"]
