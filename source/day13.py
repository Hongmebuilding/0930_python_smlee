"""
    Day13 Crawling
    Version : 1.0
    Created : 2021.14.10
    Updated : 2021.14.10
    Author  : S.M.Lee
"""
import requests # requests class 이용할 준비
from bs4 import BeautifulSoup   # bs4 모듈에서 BS class 가져와라

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=191559#'
response = requests.get(url)    # 객체 생성 # 웹페이지 가져오기
html = response.text
soup = BeautifulSoup(html, 'html.parser')   # 문법 규칙에 따라 단어를 분석하는것

res = soup.find('div')
res2 = soup.find('div').text
res3 = soup.find('div').get('id')   # find는 맨 처음 한개만 찾는다
print(res)
#print(res2)
print(res3)

list = soup.find_all('div', class_='tx_top')    # div 태그에 속성이 tx_top인거 다 갖고와라
print(list)

for idx, str in enumerate(list):    # 글머리(idx) 붙이기 # list로 하면 content를 꺼내옴
    print(idx+1, str.find('strong').text)   # strong으로 둘러쌓인 text 가져와라

list2 = soup.find('p', class_='con_tx')
print(list2.text)

list3 = soup.find_all('h5')
print('****** 한 줄 이야기 요약 *******')
print(list3[0].text)

# url = 'http://finance.naver.com/item/frgn.naver'
url = 'https://finance.naver.com/item/main.naver?code=005930'
param = {'code':'005930', 'page':'1'}
response = requests.get(url, params=param)
response = requests.get(url)
print(response.text)
