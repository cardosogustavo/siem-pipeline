import sqlite3
import pandas as pd

DB_PATH = 'sqlite_loader/siem_logs.db'

conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query("SELECT * from siem_logs LIMIT 100", conn)

print("Data read successfully")
print(df.head())


# estatísticas rápidas
print("\n contagem de endereços ip por niveis de log: ")
print(df['ip_address'].value_counts())