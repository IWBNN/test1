import MySQLdb

conn = MySQLdb.connect(
    user="crawl_usr",
    passwd="Test001",
    host="localhost",
    db="crawl_data"
    # charset="utf-8"
)
cursor = conn.cursor()
bookname = "처음 시작하는 파이썬"
url_name = "www.wikibook.co.kr"
cursor.execute(f"INSERT INTO books VALUES(\"{bookname}\",\"{url_name}\")")
conn.commit()