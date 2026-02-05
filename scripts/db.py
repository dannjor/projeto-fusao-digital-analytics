from sqlalchemy import create_engine
from config import DATABASES
import urllib

def get_postgres_engine():
    db = DATABASES['postgres_cloud']
    conn_str = (
        f"postgresql+psycopg2://{db['user']}:{db['password']}@"
        f"{db['host']}:{db['port']}/{db['database']}"
    )
    return create_engine(conn_str)

def get_sqlserver_engine():
    db = DATABASES['sqlserver_local']
    params = urllib.parse.quote_plus(
        f"DRIVER={{{db['driver']}}};"
        f"SERVER={db['server']};"
        f"DATABASE={db['database']};"
        f"UID={db['UID']};"
        f"PWD={db['PWD']};"
        f"Encrypt={db['Encrypt']}"
    )
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
