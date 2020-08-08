class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         super().__init__()


## 위와 같이 드랍쉽을 생성하려고 정의한 FlyableUnit() 사용했더니,
## 결과는 Flyable()에서 정의한 "Flyable 생성자"가 출력되었다.
## 이는 super() 사용시 클래스 FlyableUnit(Flyable, Unit)에서 정의한것과 같이,
## 먼저 상속으로 정의한 Flyable이 작동한다. 
## super()는 상속에 순서에 영향을 끼친다는 점 때문에 다중 상속 시에는

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

## 위와 같이, 이렇게 사용하는 것이 좋다.

# 드랍쉽 생성
dropship = FlyableUnit()



# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
#   강남 아파트 매매 10억 2010년
#   마포 오피스텔 전세 5억 2007년
#   송파 빌라 월세 500/50 2000년

#[코드] 4:46:30
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물정보 표시
    def show_detatil(self):
        print(self.location, self.house_type, self.deal_type,\
        self.price, self.completion_year)

houses = []
house_1 = House("강남", "아파트", "매매", "10억", "2010년")
house_2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house_3 = House("송파", "빌라", "월세", "500/50", "2000년")

# for i in range(1,4):
#     houses.append(house)
houses.append(house_1)
houses.append(house_2)
houses.append(house_3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detatil()



