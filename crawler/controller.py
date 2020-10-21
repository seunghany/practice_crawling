import requests

res = requests.get("https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%B3%91%ED%97%8C")
res.raise_for_status() # 오류 발생시 에러
print("응답코드 :", res.status_code) # 200 이면 정상, 403 이면 접근 불가능
print('웹 크롤링이 진행합니다')


print(len(res.text))
# with open("mywiki.html", "w", encoding='utf8') as f:
#     f.write(res.text)
# 파일에 있는 html 다 갖고 오는 방법 파일도 새로 하나 만듬