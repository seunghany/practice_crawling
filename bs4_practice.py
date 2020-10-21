import requests
from bs4 import BeautifulSoup
url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%B3%91%ED%97%8C"
# url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # 혹시 문제가 있을시

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text()) # 정보 다보여줌
# print(soup.table) # 첫 테이블을 보여줌
# print(soup.table.attrs) # 테이블 안에 있는 것들 # ['infobox', 'infobox', 'vcard', 'vevent']
# print(soup.table.findall('td'))

# print(soup.find('table', attrs = {"class":"infobox"}))
table = soup.find('table', attrs = {"class":"infobox"})
# print(table.td.img.src)
# print(table.get_text())
# print(table.tr)
# print(table.tbody.tr.get_text())

# next_tr = table.tr.find_next_sibling("tr")
# print(next_tr)
# print("--" * 50)
# next_tr = table.tr.find_next_sibling("tr")
# print(next_tr)
# print(table.tbody.tr.next_sibling.next_sibling.get_text())
tables = table.find_all("tr")
name = tables[0].get_text()

tables = tables[2:]
actor = {}
for table in tables:
    th = table.th.get_text()
    td = table.td.get_text()
    actor[th] = td

print(actor)
print("***" * 50)
actors = {}
actors[name] = actor
print(actors['이병헌'])
