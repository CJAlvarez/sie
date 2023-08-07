import pyodbc


# conn = pyodbc.connect("DRIVER={FreeTDS};SERVER=192.168.0.4;DATABASE=KIELSA28;UID=sa;PWD=123;unicode_results=True;")
# cur = conn.cursor()
# cur.execute("select * from item")


# import pyodbc
#
# dsn = 'FreeTDS'
# user = '<sa>'
# password = '<123>'
# database = '<KIELSA28>'
#
# con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
# cnxn = pyodbc.connect(con_string)

# connectionString = 'DSN=sqlserverdatasource;UID=sa;PWD=123;DATABASE=KIELSA28'
connectionString = 'DRIVER={FreeTDS};SERVER=192.168.21.32\\SRV_WHERNANDEZ;DATABASE=siedatabaseok;UID=sa;PWD=123;'
connection = pyodbc.connect(connectionString)


query = "SELECT cecap_nombre FROM  CatCecaps"

cnxn = pyodbc.connect(connectionString)

cursor = cnxn.cursor()
cursor.execute(query)

row = cursor.fetchall()
print (row)
print(query)