"""
    Day14 Visualization
    Version : 1.0
    Created : 2021.12.16
    Updated : 2021.12.16
    Author  : S.M.Lee
"""

# list example
alist = [1, 2, 3, 4, 5]
print(alist)
print(len(alist))

blist = [1, 2, [3, 4], 5]
print(blist)
print(len(blist))

blist.append(6)  # 맨 뒤에 6을 추가
blist.insert(1, 7)  # 1번 인덱스 자리에 7을 추가
blist.pop()  # 맨 뒤의 데이터를 꺼내고 삭제
blist.pop(0)  # 0번 인덱스 자리의 데이터를 꺼내고 삭제
print(blist)

clist = [100, 200, 300, 400, 500]
dlist = clist[::-1]  # 배열을 역순으로 복제
print(dlist)

# list Challenge 1
list1 = ['M', 'na', 'i', 'Ke']
list2 = ['y', 'me', 's', 'lly']

# 결과 = ['My', 'name', 'is', 'Kelly']
# solution0
res = [list1[0]+list2[0], list1[1]+list2[1]]
print(res)
print('.')

# solution1
res = []
for i in range(len(list1)):
    res.append(list1[i]+list2[i])
print(res)
print('.')

# solution2
res = [i+j for i, j in zip(list1, list2)]   # zip이 묶어주는 역할
print(res)

for i, j in zip(list1, list2):
    print(i, j)

for i, j in zip(list1, list2):  # 튜플???
    print(i)

for i, j in zip(list1, list2):
    print(i+j)

res = [i+j for i, j in zip(list1, list2)]   # 일대일 대응
print(res)
print('.')

# list Challenge 2
list5 = [1, 2, 3, 4, 5]
# solution
res = [i*i for i in list5]  # 수식 == 미지수
print(res)
print('.')

# list Challenge 3
list7 = ['Hello', 'Mike']
list8 = ['Bye', 'Sleep']
print('.')

# res = ['Hello Bye', 'Mike Sleep']
res = [i+' '+j for i,j in zip(list7, list8)]
print(res)
print('.')

# res = ['Hello Bye', 'Hello Sleep', 'Mike Bye', 'Mike Sleep']
res = [i+' '+j for i in list7 for j in list8]
print(res)
print('.')

# list Challenge 4
list10 = [10, 20, 30, 40]
list11 = [100, 200, 300, 400]
print('.')

""" res
10 400
20 300
30 200
40 100
"""

for i, j in zip(list10, list11[::-1]):
    print(i, j)

# list Challenge 5
list12 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]    # 0~1/2~3은 list가 아니다
                                                            #           int이다.
print(list12[2])
print(list12[2][2])
list12[2][2].append(7000)
print(list12)
print('.')

# list Challenge 6
list13 = [5, 10, 15, 20, 25, 30, 20]


# 첫 번째 나온 20을 200으로 변경
list13[list13.index(20)] = 200
print(list13)
print('.')

list13 = [5, 10, 15, 20, 25, 30, 20]
# 두 번째 나온 20을 200으로 변경
list13[list13.index(20, list13.index(20)+1)] = 200  # index(int, ~부터)
print(list13)
print('.')
