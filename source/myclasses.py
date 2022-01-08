class House:
    """
그냥 만들어본 것(아무 의미 없음)
    """
    house_count = 0

    def __init__(self, name):   # 변수 있으면 돌고
        print("새로운 집이 생성되었습니다.")
        self.name = name
        House.house_count += 1

    def __init__(self):     # 변수 없어도 돌고   # 상수 형태는 str, int
        print("새로운 집이 생성되었습니다.")
        self.name = "이름없어"

class Apart:
    def __init__(self):
        print("새로운 아파트가 만들어졌습니다.")
        self.room = 3
        self.furniture = []

    def setRoom(self, i):   # instance
        self.room = i

    def getRoom(self):
        return self.room

    def addFurniture(self, *str):   # str이 몇 개 들어오는지 모른다
        self.furniture.append(str)

    def getFurniture(self):
        return self.furniture