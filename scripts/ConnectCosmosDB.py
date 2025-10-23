import pyodbc
# This script is an Integrated connection, only will work on a domain joined machine
# with a user logged in with proper permissions. Not personal computers.
conn_str = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=cosmosdbsrv2.database.windows.net;"
    "Database=CCSQLDB_02;"
    "Authentication=ActiveDirectoryIntegrated;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)


with pyodbc.connect(conn_str) as conn:
    print("Connected successfully!")

