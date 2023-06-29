import MySQLdb
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    RANK = 100  # 일단 100으로 설정한 후 상황 보기

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get("https://suwings.syu.ac.kr/websquare/websquare.html?w2xPath=/scr/system/main.xml",
                       headers=header)  # 사이트 크롤링 주소
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')

    SBJT_NM = parse.find_all("div", {"class": "ellipsis rank01"})
    STFNM = parse.find_all("div", {"class": "ellipsis rank02"})

    title = []
    pname = []

    for t in SBJT_NM:
        title.append(t.find('a').text)

    for p in STFNM:
        pname.append(p.find('span', {"class": "checkEllipsis"}).text)
    items = [item for item in zip(title, pname)]

conn = MySQLdb.connect(
    user="crawl_usr",
    passwd="Test001",
    host="localhost",
    db="crawl_data"
    # charset="utf-8"
)
# 커서 생성
cursor = conn.cursor()

# 실행할 때마다 다른값이 나오지 않게 테이블을 제거해두기
cursor.execute("DROP TABLE IF EXISTS TT")

# 테이블 생성하기
cursor.execute("CREATE TABLE TT (`rank` int, title text, url text)")
i = 1
# 데이터 저장하기
for item in items:
    cursor.execute(
        f"INSERT INTO melon VALUES({i},\"{item[0]}\",\"{item[1]}\")")
    i += 1

# 커밋하기
conn.commit()
# 연결종료하기
conn.close()