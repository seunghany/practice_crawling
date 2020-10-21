import re # 정규식 
# 951003 - 11*****
# 010 3026 7801
# 11가 1234
# 이런 형태가 정규식

p = re.compile("ca.e")
# . : 하나의 문자 의미 (a, b, c, d, e)
# ^ 문자열의 시작 (^de) -> desk, destiondation (o) | fade(x)
# $ 문자의 끝 -> (se$) case, base (o) | face(x)

def print_match(m):
    if m:
        print(m.group())
    else:
        print('매칭 안됨')
txt = "ca1e, ess"
print(p.match(txt))
m = p.match(txt)
print_match(m)

# 정규식 정리

# 1. import re
# 2. p = re.compile("원하는 형태") : 
# 3. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
# 4. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
# 5. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 "리스트" 형태로 반환

# . : 하나의 문자 의미 (a, b, c, d, e)
# ^ 문자열의 시작 (^de) -> desk, destiondation (o) | fade(x)
# $ 문자의 끝 -> (se$) case, base (o) | face(x)

# 정규식 더 공부 하고 싶으면 밑 싸이트 ㄱㄱ 
# w3school -> python > RegEx
# python re 