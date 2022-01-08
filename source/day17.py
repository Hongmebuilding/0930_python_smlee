"""
    Day17 Numpy
    Version : 1.0
    Created : 2021.12.23
    Updated : 2021.12.23
    Author  : S.M.Lee
"""
import numpy as np
import myutils as mu

# 7. Unique
mu.cprintTitle('7. Unique')
rd = np.random.randint(1, 10, size=(3, 4))
print(rd)
numbers, counts = np.unique(rd, return_counts=True) # True가 있어야 두개 return
print('unique한 값:', numbers)
print('unique한 개수:', counts)
numbers = np.unique(rd)
print('unique한 값:', numbers)

# 8. concatenate
mu.cprintTitle('8. concatenate')
na1 = np.random.randint(10, size=(2, 3))
na2 = np.random.randint(10, size=(3, 2))
na3 = np.random.randint(10, size=(3, 3))

print(na1)
print(na2)
print(na3)
print('1) 세로 결합')
c_con = np.concatenate((na1, na3), axis=0)  # 인자 () 한개로 취급
print(c_con)

print('2) 가로 결합')
r_con = np.concatenate((na2, na3), axis=1)  # axis 는 행렬자체를 인덱스로 본다.
print(r_con)

# 9. split
mu.cprintTitle('9. split')
r = np.arange(11, 20)
print(r)
array1 = np.split(r, [5])   # index위치부터 나눔
print(array1)
array2 = np.split(r, [2, 4, 6, 8])
print(array2)
aa = array2[0]
print(aa)

# 10. sort
mu.cprintTitle('10. sort')
r1 = np.random.randint(10, size=(3, 3))
print(r1)

# row sort
r1.sort()
print('row sort')
print(r1)

# column sort
r1.sort(axis=0)
print('column sort')
print(r1)

# 배열 타입 바꾸기
mu.cprintTitle('11. astype')
r = np.random.randint(1, 5, 10)
print(r, r.dtype)
r2 = r.astype(float)
print(r2, r2.dtype)
r3 = r.astype(str)
print(r3, r3.dtype)

"""
Quiz 5
1에서 20까지의 랜덤숫자를 갖는 5 * 5 행렬을 만드는데,
최소값에는 '값(MIN)', 최대값에는 '값(MAX)'
"""
print()
mu.cprintTitle('Q5')
nd = np.random.randint(1, 21, size=25)
print(nd)
# nd.argmax() : 최대값이 두 개 이상 존재할 때 불가
# nd.argmin() : 최소값이 두 개 이상 존재할 때 불가
maxv = str(nd.max())
minv = str(nd.min())

sd = nd.astype(str)
for i in range(sd.size):
    if sd[i] == maxv:
        sd[i] += '(MAX)'
    if sd[i] == minv:
        sd[i] += '(MIN)'

fd = sd.reshape(5,5)
print(fd)

"""
Quiz 6
100부터 130까지의 랜덤숫자를 가지는 8 * 8 행렬을 만들고
3의 배수에는 'fiz', 5의 배수에는 'buz', 15의 배수에는 'fbz'를 출력
"""
print()
mu.cprintTitle('Q6-1')
rd = np.random.randint(100, 131, size=64)
for i in range(rd.size):
    if rd[i] % 3 == 0:
        rd[i] += 4000
    if rd[i] % 5 == 0:
        rd[i] += 3000
    if rd[i] % 15 == 0:
        rd[i] += 2000
rd = rd.astype(str)
for i in range(rd.size):
    if rd[i] > '4000':
        rd[i] = 'fiz'
    if rd[i] > '3000':
        rd[i] = 'buz'
    if rd[i] > '2000':
        rd[i] = 'fbz'

rd = rd.reshape(8, 8)
print(rd)

# print(eval('3*3')) -> str을 받고 int로 돌려줌
print()
mu.cprintTitle('Q6-2')
na = np.random.randint(100, 131, 64)
sa = na.astype(str)
for i in range(sa.size):
    if eval(sa[i]) % 15 == 0:
        sa[i] = 'fbz'
    elif eval(sa[i]) % 5 == 0:
        sa[i] = 'buz'
    elif eval(sa[i]) % 3 == 0:
        sa[i] = 'fiz'
ra = sa.reshape(8, 8)
print(ra)

print()
mu.cprintTitle('basic calculation')
print('list')
ls = [1, 2, 3]
print(ls, ls * 3)
print('ndarray')
na = np.array([1, 2, 3])
print(na, na * 3)
nb = np.array([4, 5, 6])
print(nb, 'na * nb :', na * nb)

print()
mu.cprintTitle('compare calculation')
print(na)
print(nb)
print('na == 2, nb > 4', na == 2, nb > 4)

print()
mu.cprintTitle('filtering')
print('na ->', na)
print('na[na==2]', na[na==2])   # True 인것만 나옴
print(na[[False,True,False]])

na3 = np.array([1, 2, 3, 2, 2])
print('na3[na3==2] ->', na3[na3==2])
print('nb[nb>4]',nb[nb>4])

print()
print('3의 배수만 출력')
na4 = np.arange(10)
print(na4)
print(na4[na4%3==0])

# 두 개의 ndarray에서 같은 데이터만 남기기
na1 = np.array([1, 2, 3, 4, 5])
na2 = np.array([1, 0, 3, 0, 5])
print(na1)
print(na2)
print(na1 == na2)
print('na1[na1==na2] ->', na1[na1==na2])

print()
mu.cprintTitle('broadcasting')
na = np.array(range(12)).reshape(3, 4)
print('na : ')
print(na)

# 모든 데이터에 1을 더함
print(na + 1)

# 모든 형에 na1 벡터 데이터가 더해짐
print()
na1 = np.array(range(4))
print(na)
print(na1)
print(na + na1)

print()
na2 = np.array([[0], [1], [2]]) # 3행 1열
print('na :')
print(na)
print('na2 :')
print(na2)
print('na + na2 :')
print(na + na2)
