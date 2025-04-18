import pandas as pd
import sqlite3
import os

# caminho dos arquivos parquet (visto dentro do container)
parquet_path = "/app/output/parquet"
db_path = "/app/siem_logs.db"

def read_parquet_files(parquet_path):
    dataframes = []
    for root, _, files in os.walk(parquet_path):
        for file in files:
            if file.endswith(".parquet"):
                file_path = os.path.join(root, file)
                print(f"Reading {file_path}")
                df = pd.read_parquet(file_path, engine='fastparquet')
                dataframes.append(df)
    return pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()

def save_to_sqlite(df, db_path):
    conn = sqlite3.connect(db_path)
    df.to_sql("siem_logs", conn, if_exists="append", index=False)
    conn.commit()
    conn.close()
    print(f"Saved {len(df)} rows to {db_path}")

if __name__ == "__main__":
    df = read_parquet_files(parquet_path)
    if not df.empty:
        save_to_sqlite(df, db_path)
    else:
        print("No parquet files found")