# 메서드 오버라이딩
# pr13의 스타크래프트 이어서...

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
        .format(self.name, location, self.speed)) 

class AttackUnit(Unit): # Unit 클래스 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        #super().__init__(name, hp, speed) #super()를 활용해서 위와같은 기능으로 표현가능
        self.damage = damage               ## 다만, super() 사용시, self는 쓰지 않음!!! 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}"\
        .format(self.name, location, self.damage)) # 클래스에서 정의된 멤버변수는 self.사용!

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self. hp <= 0:
            print("{0} 파괴되었습니다.".format(self.name))

class Flyable: # 공중유닛 정의
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
        .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): #공중공격 유닛 정의
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed) # 공중유닛 초기화

    def move(self, location):
        print("[공중유닛 이동]")
        self.fly(self.name, location) # Flyable()에서 상속받은 fly() 함수를 사용!


# 벌처 생성: 지상 유닛, 기동성이 좋음
valture = AttackUnit("벌처", 80, 10, 20) 

# 배틀크루저 생성: 공중 유닛, 체력 공격이 굉장히 좋음
battlecruser = FlyableAttackUnit("배틀크루저", 500, 25, 3) #체=500, 공격=25, flying_speed=3

valture.move("11시")
battlecruser.fly(battlecruser.name, "11시") # Flyable 클래스에는 name 정보가 따로 정의되어있지 않으므로
## 자 위에 두줄에서 살피듯이 벌처나 배틀크루저를 만들때마다 move()와 fly()를 사용하게 되면서
## 이게 지상유닛인지 공중유닛인지를 프로그래머가 알아야하는 상황이온다.
## 편리한 사용을 위해 지상유닛은 이동을 하고, 공중유닛은 날아갈수 있도록 처리해야 한다.
## 이럴때, "메서드 오버라이딩"을 사용하게 된다!! -> FlyableAttackUnit()에서 move() 새롭게 재정의
## --> 그래서 FlyableAttackUnit()에서 move()를 정의
battlecruser.move("9시")


