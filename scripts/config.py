# config.py

DATABASES = {
    'postgres_cloud': {
        'host': 'database-empresa-b.cs5w6cyu0cgy.us-east-1.rds.amazonaws.com',
        'port': 5432,
        'user': 'postgres',
        'password': 'postgres123',
        'database': 'postgres'
    },
    'sqlserver_local': {
        'server': 'DESKTOP-BSS415J\SQLEXPRESS01',
        'database': 'database_empresa_a',
        'driver': 'ODBC Driver 18 for SQL Server',
        'UID': 'airflow_user',
        'PWD': 'zse$5rdX01',
        'Encrypt': 'no'
    }
}