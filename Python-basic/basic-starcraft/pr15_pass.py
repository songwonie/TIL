# pass

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
        .format(self.name, location, self.speed)) 

# 건물 생성
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # pass의 의미는 아무것도 안하고, 일단 넘어간다 라는 의미!

# 서플라이디폿 생성 : 건물 생성시 유닛 8 생산 사능
supply_depot = BuildingUnit("서플라이디폿", 500, "7시")


