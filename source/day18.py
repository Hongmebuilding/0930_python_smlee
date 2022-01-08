"""
    Day18 Pandas
    Version : 1.0
    Created : 2021.12.28
    Updated : 2021.12.28
    Author  : S.M.Lee
"""

import pandas as pd
import myutils as mu
import numpy as np

# 1. Series
mu.cprintTitle("1. Series")
# (1) 스칼라(Scalar) 데이터
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0])
print(s)
print()
lista = range(1, 50)
s1 = pd.Series(7, index=lista)    # index 배열 타입 된다. None은 없다
print(s1)

# (2) 일차원 배열 데이터
s2 = pd.Series(np.random.randn(5))
print(s2)
print()
s3 = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s3)
print()

# (3) 리스트 데이터
s4 = pd.Series([1, 2, 3, 4, 5], index=['봄', 'ddd', 'c', 'd', 'e'])
print(s4)
print()

# (4) 딕셔너리 데이터
s5 = pd.Series({'a':0, 'b':1, 'James':2})
print(s5)
print()

mu.cprintTitle("2. date_range")
# start-end를 지정
date1 = pd.date_range(start='2021-01-01', end='2021-01-10')
print(date1)

# start-period를 지정
date2 = pd.date_range(start='2021-01-01', periods=7)
print(date2)
print()

# 2일씩 증가하는 날짜 생성
date3 = pd.date_range(start='2021-01-01', periods=10, freq='2D')
print(date3)
print()

# 1시간 주기로 10시간을 생성
date4 = pd.date_range(start='2021-01-01 08:00', periods=10, freq='H')
print(date4)
print()

# 30분 단위로 4개 시간
date5 = pd.date_range(start='2021-01-01 10:00', periods=4, freq='30MIN')
print(date5)
print()

# 10초 단위로 4개 시간
date6 = pd.date_range(start='2021-01-01 10:00', periods=4, freq='10S')
print(date6)
print()

# 3. DataFrame
mu.cprintTitle("3. DataFrame")
# (1) numpy와 2차원 배열 데이터 사용
data_list = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(data_list.shape)
print(data_list.ndim)
df1 = pd.DataFrame(data_list)
print(df1)
print()

# (2) index, column
data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(data.shape)
index_date = pd.date_range('2021-01-01', periods=4)
columns_list = ['AAA', 'AAB', 'AAC']
df2 = pd.DataFrame(data, index=index_date, columns=columns_list)
print(df2)
print()

# (3) 어느 회사의 연도 및 지사별 고객수 데이터
#     데이터가 딕셔너리 형태
data = {'연도':[2012,2016,2016,2017,2017],
        '지사':['한국','한국','미국','한국','미국'],
        '고객수':[200,250,450,300,500]}
print(data)
print()
df3 = pd.DataFrame(data)
print(df3)
print(df3.index)
print(df3.columns)
print(df3.values)
print()

# 5. Key
mu.cprintTitle('Key')
data = {'weight':[80, 70, 65, 46, 51],
        'height':[170, 180, 155, 145, 150],
        'type':['A','B','B','O','O']}
df = pd.DataFrame(data)
#몸무게 목록 추출
print('몸무게 목록')
print(df['weight'])
print()
# 키와 몸무게 목록 추출
print('키와 몸무게 목록')
print(df[['height','weight']])
print()

# 6. Slice
mu.cprintTitle('Slice')
# 2, 3번째 데이터 출력
print(df[2:4])
print()
# 2번째 데이터 출력
print(df[2:3])
print()
# 3번째 이하 데이터 출력
print(df[3:])
print()

# 7. Filter
mu.cprintTitle('Filter')
data = {'weight':[80, 70, 65, 46, 51],
        'height':[170, 180, 155, 145, 150],
        'type':['A','B','B','O','O']}
df = pd.DataFrame(data)

# 키 150이상만 추출
print('df[df.height >= 150]\n', df[df.height >= 150])
print()

# Type이 O인 것만 추출
print('df[df.type == O]', df[df.type == 'O'])
print()

# 7. Sort
mu.cprintTitle('Sort')
# height로 정렬(작은 -> 큰)
print(df.sort_values(by='height'))
print()
# weight로 정렬(큰 -> 작은)
print(df.sort_values(by='weight', ascending=False))

# 8. Rot
mu.cprintTitle('Rot')
data = [['A', 'B', 'C'],['D', 'E', 'F'],['G', 'H', 'I']]
df = pd.DataFrame(data)
print(df)
print("이크 행과 열이 바뀌었네")
print(df.T)

# 응용편
KTX_Data = {'경부선':[39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선':[7313, 6967, 6873, 6626, 10622, 9928, 5526],
            '경전선':[3627, 4168, 4888, 4424, 4606, 4984, 5570],
            '동해선':[np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]}
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_Data, index=index_list)
print(df_KTX)

# 1. DataFrame 출력
mu.cprintTitle('1. DataFrame 출력')
print(df_KTX)
# 2. index 출력
mu.cprintTitle('2. index 출력')
print(df_KTX.index)
# 3. column 출력
mu.cprintTitle('3. column 출력')
print(df_KTX.columns)
# 4. data 출력
mu.cprintTitle('4. data 출력')
print(df_KTX.values)
# 5. 첫 n개 행 출력
mu.cprintTitle('5. 첫 n개 행 출력')
print(df_KTX.head()) # 인자가 없으면 5
print(df_KTX.head(3)) # 첫 번째 3행
mu.cprintTitle('7. 1번행 데이터 출력')
print(df_KTX[0:1])
mu.cprintTitle('8. 2~4번행 데이터 출력')
print(df_KTX[1:4])
mu.cprintTitle('9. 2011년 행 데이터 출력')
print(df_KTX.loc['2011'])
mu.cprintTitle('10. 2013년부터 2016까지 행 데이터 출력')
print(df_KTX.loc['2013':'2016'])





