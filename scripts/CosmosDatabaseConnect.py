import pyodbc

try:
    conn = pyodbc.connect(
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=cosmosdbsrv2.database.windows.net;"
        "Database=CCSQLDB_02;"
        "Authentication=ActiveDirectoryIntegrated;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    print("Connected successfully with Azure AD Integrated Login!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)