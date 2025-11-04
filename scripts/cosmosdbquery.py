import pandas as pd
from sqlalchemy import create_engine
import urllib

params = urllib.parse.quote_plus(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=cosmosdbsrv2.database.windows.net;"
    "Database=CCSQLDB_02;"
    "Authentication=ActiveDirectoryIntegrated;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)
engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)


while True:
    request_type = input("Enter the Request Type: 1 for 'Job Material Lot', or 2 for 'FG Material List': ").strip()
    if request_type == "1":
        request_type = "job material lot"
        break
    elif request_type == "2":
        request_type = "fg material list"
        break
    else:
        print("Invalid input. Please enter; 1 for 'Job Material Lot', or 2 for 'FG Material List'.")

if request_type == "job material lot":
    while True:
        job_number = input("Enter the Job Number you wish to know the Material Lot(s) of (e.g. JM9456, JB19456): ").strip().upper()
        if len(job_number) < 10:
            job_number = job_number[:2] + job_number[2:].zfill(8)
            break
        elif len(job_number) > 10:
            print("Job Number is too long. Please enter a valid Job Number.")
            continue
        else:
            break

elif request_type == "fg material list":
    while True:
        item_number = input("Enter the Item Number you wish to know the Material List of: ").strip().upper()
        if item_number:
            break
        else:
            print("Invalid entry. Please enter a valid Item Number.")
else:
    print("Invalid Request Type")

if request_type == "job material lot":
    query = f"""
    SELECT item, lot,
        FORMAT(ABS(SUM(qty)), 'N2') + ' lbs' AS total_qty,
            FORMAT((ABS(SUM(qty)) * 100.0) / SUM(ABS(SUM(qty))) OVER (PARTITION BY item), 'N2') + ' %' AS pct_share
    FROM ERP_Reporting.matltran_mst
    WHERE [ref_num] COLLATE SQL_Latin1_General_CP1_CI_AS = '{job_number}'
    AND [lot] <> ''
    GROUP BY item, lot
    ORDER BY item, lot;
    """
    df = pd.read_sql(query, engine)
    print(f"Here are the material lots for {job_number}:")
    print(df)

elif request_type == "fg material list":
    query = f"""
    ;WITH FirstRef AS (
        SELECT TOP 1 ref_num
        FROM ERP_Reporting.matltran_mst
        WHERE [item] COLLATE SQL_Latin1_General_CP1_CI_AS = '{item_number}'
        AND [trans_type] = 'F'
        ORDER BY ref_num
)
    SELECT DISTINCT m.[item]
    FROM ERP_Reporting.matltran_mst AS m
    INNER JOIN FirstRef f ON m.ref_num = f.ref_num
    WHERE m.[trans_type] = 'I';
    """
    
    df=pd.read_sql(query, engine)
    print(f"Here is the material list for {item_number}:")
    print(df)