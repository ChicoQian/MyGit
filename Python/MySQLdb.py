import MySQLdb

conn = MySQLdb.Connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            passwd = '',
            db = 'renliu',
            charset = 'utf8'
)
cursor = conn.curosr()

print conn
print cursor

cursor.close()
conn.close()