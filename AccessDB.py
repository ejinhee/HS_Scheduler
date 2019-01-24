import pyodbc



def AccessDB(server, database, username, password):
    SV = server
    DB = database
    UID = username
    PWD = password
    con_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s"%(SV, DB, UID, PWD)
    cnxn = pyodbc.connect(con_string)
    cursor = cnxn.cursor()
    return cursor