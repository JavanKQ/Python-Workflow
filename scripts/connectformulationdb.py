import pyodbc
conn_str = r"Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=\\stl22\Formulation\formulation.accdb;"
with pyodbc.connect(conn_str) as conn:
    print("Connected!")