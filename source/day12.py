"""
    Day2 Class, Exception
    Version : 1.0
    Created : 2021.12.09
    Updated : 2021.12.09
    Author  : S.M.Lee
"""

import myclasses as mc

myhouse = mc.House()
print("우리 집 개수 : {}".format(myhouse.house_count))
yourhouse = mc.House()
print("우리 집 개수 : {}".format(myhouse.house_count))
print("너희 집 개수 : {}".format(yourhouse.house_count))
myhouse.house_count = 5043  # class 변수 건들임
print("우리 집 개수 : {}".format(myhouse.house_count))
print("너희 집 개수 : {}".format(yourhouse.house_count))
hishouse = mc.House()
print("우리 집 개수 : {}".format(myhouse.house_count))
print("너희 집 개수 : {}".format(yourhouse.house_count))
print("그의 집 개수 : {}".format(hishouse.house_count))
print(hishouse.name)

# 클래스명.__doc__으로 해당 클래스의 설명을 볼 수 있다.
print(mc.House.__doc__)

apart1 = mc.Apart()
apart2 = mc.Apart()
print("방 개수", apart1.getRoom()) # 객체이름.함수이름(넣고자x)
apart1.setRoom(4)   # 객체이름.함수이름(넣고자x)
print("방 개수", apart1.getRoom())
apart1.addFurniture("Sofa")
apart1.addFurniture("TV")
apart1.addFurniture("Bed")
print(apart1.getFurniture())
print(apart2.getFurniture())

a = []
a.append(apart1)
print(a[0]) # class의 데이터가 들어가있는다.
a.append(1)
a.append("jwlee")
print(a)

import myutils as mu
mu.cprintTitle("Standard Exception")
while True:
    try:
        a = int(input("나누어지는 정수를 입력하세요 :"))
        if a > 10000:
            raise Exception("장난하냐")
        b = int(input("나눌 정수를 입력하세요 :"))
        c = a / b
    except ZeroDivisionError as e:
        print("0으로 나눌려고 하냐?")
        print(e)
        continue
    except ValueError as e:
        print("정수만 된다니까")
        print(e)
        continue
    except Exception as e:
        print(e)
        print("오류났어")
        continue
    else:  # 오류 무
        print("오류 안나고 정상수행되었네요")
        print("{}/{} = {}".format(a, b, c))
        break
    finally:  # default
        print("오류 나든 안나든 잘하신 건 없습니다")

mu.cprintTitle("User Exception")
def myexcept():
    raise Exception("호출하기만 해봐라")

try:    # raise 일지라도 try 안에 있으면 처리 가능하다
    myexcept()
except Exception as e:

    print("긴급상황긴급상황")
    print(e)

print(Exception.__doc__)    # 모든 Exception
