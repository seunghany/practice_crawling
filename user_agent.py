import requests
url  = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%B3%91%ED%97%8C"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
# res = requests.get("http://nadocoding.tistoy.com")
res = requests.get(url, headers=headers)
res.raise_for_status() # 오류 발생시 에러
print("응답코드 :", res.status_code) # 200 이면 정상, 403 이면 접근 불가능
print('웹 크롤링이 진행합니다')
