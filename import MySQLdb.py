import MySQLdb

conn = MySQLdb.connect(
    user="crawl_usr",
    passwd="Test001",
    host="localhost",
    db="crawl_data"
    # charset="utf-8"
)
print(type(conn))
# <class 'MySQLdb.connections.Connection'>
cursor = conn.cursor()
print(type(cursor))
# <class 'MySQLdb.cursors.Cursor'>
cursor.execute("CREATE TABLE books (title text, url text)")
conn.commit()