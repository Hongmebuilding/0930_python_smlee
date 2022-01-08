"""
    Day16 Numpy
    Version : 1.0
    Created : 2021.12.17
    Updated : 2021.12.17
    Author  : S.M.Lee
"""
import numpy as np
import myutils as mu

# 1. 행렬의 생성 1
mu.cprintTitle('1-1) 1차원 행렬')
array = np.array([1, 2, 3])
array2 = np.array(range(5))
print(array)
print(array2)

mu.cprintTitle('2) 2차원 행렬')
array = np.array([[1,2,3],[4,5,6]])

mu.cprintTitle('3) 3차원 행렬')
array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,np.NaN]]])
# nan이라는 미지수가 얼마나 클지 모르기에 모든 정수가 실수타입으로 처리됨 ex) 7.
print(array)

mu.cprintTitle('4) 4차원 행렬의 차원과 모양')
print('차원', array2.ndim, '모양', array2.shape)

mu.cprintTitle('5) 행렬의 모양 변경')
na = np.array(range(10))    # 10*1 array # 10행 1열 (세로)
print('길이:', len(na))
nb = na.reshape(2, 5)
print('길이:', len(nb))   # 2*5 array
nc = np.array(range(36))
nd = nc.reshape(3, 3, 4)
print('길이:', len(nd))

# 2. 행렬 데이터의 선택
mu.cprintTitle('2. 행렬 데이터의 선택')
array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,np.NaN]]])
print(array)
print('길이:', len(array))    # 2

mu.cprintTitle('1) 데이터의 선택')
print('array[1] : \n', array[1])
print('array[1][0] :', array[1][0])
print('array[1][0][2] :', array[1][0][2])

mu.cprintTitle('2) [] 생략가능')
print('array[1,0,2] : ', array[1,0,2])

mu.cprintTitle('3) 범위로 선택 가능')
print('array[1:, :, :2} :\n', array[1:, :, :2]) # 마지막은 2미만
print('array[1:, :, 1:] :\n', array[1:, :, 1:]) # 마지막은 1초과
print('array[1:1, :, 1:] :\n', array[1:1, :, 1:]) # 빈 깡통. 첫번째에서 걸러짐
print(array[1:, :, :1])

mu.cprintTitle('4) 데이터 수정')
ls = np.array(range(5)) # 5*1
ls[2] = 0.9
print(ls)   # 정수 타입이여서 0으로 나옴

ls = np.array(range(5), dtype='float')
ls[2] = 0.9
print(ls) # line57 개선

mu.cprintTitle('5) 브로드캐스팅 수정')
ls = np.array(range(5))
print('변경 전 ls : ', ls)
ls[3:] = 0
print('변경 후 ls : ', ls)

# 3. 행렬 데이터의 생성2
mu.cprintTitle('3. 행렬 데이터의 생성 2')
print('1) zeros')
zero = np.zeros((2, 3))
print('np.zero((2,3)) : \n', zero)
print()
print('2) ones')
ones = np.ones((4, 3), dtype=int)
print('np.ones((4,3), dtype=int) :')
print(ones)
"""
Q1.
5개의 1로 이루어진 1차원 행렬(벡터)을 만드시오.
[1, 1, 1, 1, 1]
"""
print('Q1')
ones = np.ones((1,5), dtype=int)
print(ones[0])
"""
Q2. 
10개의 1로 만들어진 정수 데이터 타입의 벡터에서 마지막 3개는 5로 바꾸시오.
[1, 1, 1, 1, 1, 1, 1, 5, 5, 5]
"""
print('Q2')
ones1 = np.ones((1,10), dtype=int)[0]   # 1차원은 default
ones1[7:] = 5
print(ones1)

# 4. arange
print('4. arange')
ar1 = np.arange(10)
ar2 = np.arange(5, 10)
ar3 = np.arange(5, 10, 2)
print(ar1)
print(ar2)
print(ar3)
print(type(range(5)))

# 5. linspace, logspace
print()
print('5. linspace, logspace')
# 0 ~ 100까지를 5개로 분할
lin = np.linspace(0, 100, 5)
log = np.logspace(0, 2, 5)
print('linspace :', lin)
print('logspace :', log)

"""
Q3.
1에서 10까지의 홀수 데이터를 갖는 벡터를 만드시오.
[1, 3, 5, 7, 9]
"""
print('Q3')
data = np.arange(1, 10, 2)
print(data)
"""
Q4.
0부터 8까지의 값을 갖는 3*3 행렬을 만드시오.
"""
print('Q4')
q4 = np.arange(9)
q4 = q4.reshape(3, 3)
print(q4)

# 6. Numpy Random
print()
print('6. Numpy Random')
np.random.seed(1)
result1 = np.random.randint(low=10, high=100, size=10)
print(result1)
np.random.seed(1)
result2 = np.random.randint(low=10, high=100, size=10)
print(result2)
np.random.seed(2)
result3 = np.random.randint(low=10, high=100, size=10)
print(result3)

print('2) rand')
rd = np.random.rand(100)
print(rd)

print('2) randn')
rd = np.random.randn(100) # 개수를 의미함
print(rd)

print()
print('4) randint')
rd = np.random.randint(5, 10, (2, 3))
print(rd)
rd = np.random.randint(5, size=(4, 3))  # size가 더 명쾌하다
print(rd)

print()
print('5) shuffle')
rd = np.random.randint(1, 10, size = (3, 4))
print(rd)
np.random.shuffle(rd)   # 바뀐거 알아서 들어감
print('after shuffle')
print(rd)

# 모든 차원의 데이터를 변경할 때는 1차원으로 변경 후 shuffle, 다시 원래 차원으로 복귀
print('rd.shape :', rd.shape)
print('rd.size :', rd.size)

# 1차원으로 변경
m1 = rd.reshape(rd.size)    # 1차원 default
print('after 1 dim :', m1)
# shuffle
np.random.shuffle(m1)
print('after shuffle :', m1)
# 원래 차원으로 복귀
all_shuffle = m1.reshape(rd.shape)  # m1에 rd.shape 복귀시켜라
print(all_shuffle)

print()
print('6) choice')
np.random.seed(273872)
# choice(모집단, 개수, p=확률)
c = np.random.choice([30, 20, 10, 40, 50], 5, 10, p=[0.5, 0, 0.5, 0, 0])  # %
d = np.random.choice(range(1, 6), 10, p=[0.5, 0, 0.5, 0, 0])

print(c)
print(d)