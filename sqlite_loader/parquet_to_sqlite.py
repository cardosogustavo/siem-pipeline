import pandas as pd
import sqlite3
import os
import glob

# caminho dos arquivos parquet (visto dentro do container)
parquet_path = "/app/data/parquet/*.parquet"
db_path = "/app/data/siem_logs.db"

# ler todos os arquivos parquet
parquet_files = glob.glob(parquet_path)
if not parquet_files:
    print("No parquet files found.")
    exit()

# conectar ao banco SQLite
conn = sqlite3.connect(db_path)

for file in parquet_files:
    df = pd.read_parquet(file)
    df.to_sql("siem_logs", conn, if_exists="append", index=False)

conn.commit()
conn.close()
print(f"Data inserted to {db_path}")