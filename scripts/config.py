# config.py

DATABASES = {
    'postgres_cloud': {
        'host': 'database-empresa-b.cs5w6cyu0cgy.us-east-1.rds.amazonaws.com',
        'port': 5432,
        'user': 'postgres',
        'password': '',
        'database': ''
    },
    'sqlserver_local': {
        'server': 'DESKTOP-BSS415J\SQLEXPRESS01',
        'database': 'database_empresa_a',
        'driver': 'ODBC Driver 18 for SQL Server',
        'UID': '',
        'PWD': '',
        'Encrypt': 'no'
    }

}
