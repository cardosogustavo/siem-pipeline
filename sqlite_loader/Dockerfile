FROM python:3.13-alpine

WORKDIR /app
ENV PYTHONPATH="/app"

# Instalar dependências necessárias
RUN pip install pandas fastparquet

COPY sqlite_loader/parquet_to_sqlite.py .
COPY sqlite_loader/data /app/sqlite_data

CMD ["python3", "parquet_to_sqlite.py"]