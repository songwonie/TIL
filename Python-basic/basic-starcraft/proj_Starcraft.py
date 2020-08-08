from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
        .format(self.name, location, self.speed)) 

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다".format(self.name, self.hp))
        if self. hp <= 0:
            print("{0} 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit): # Unit 클래스 상속받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        #super().__init__(name, hp, speed) #super()를 활용해서 위와같은 기능으로 표현가능
        self.damage = damage               ## 다만, super() 사용시, self는 쓰지 않음!!! 
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
        .format(self.name, location, self.damage)) # 클래스에서 정의된 멤버변수는 self.사용!

# 마린 생성
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    def steampack(self): #스팀팩 사용: hp 10 감소 대신 일정시간 동안 이동 공격속도 증가
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할수 없습니다".format(self.name))

# 탱크 생성
class Tank(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False  # 탱크의 시즈모드 개발 멤버변수

    # 시즈모드 : 개발될 시에 사용가능!
    seize_developed = False
    def set_sizmode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드로 변경!
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 상속받은 AttackUnit에서 데미지 능력치를 2배 증가
            self.seize_mode = True
        else: # 시즈모드 일때는 시즈모드를 해제!
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

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
        self.fly(self.name, location) # Flyable()에서 상속받은 fly() 함수를 사용!
        
# 레이스 생성
class Race(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        # 레이스 클로킹 
        self.clocked = False

    def clocking(self):
        if self.clocked == False: # 클로킹 모드가 아닐때는 클로킹 모드 작동!
            print("{0} : 클로킹모드로 전환합니다".format(self.name))
            self.clocked = True

        else: # 클로킹모드 시에는 클로킹 해제!
            print("{0} : 클로킹모드로 전환합니다.".format(self.name))
            self.clocked = False

def game_start():
    print("[알림] 새로운 게임을 시작합ㄴ다.")

def game_over():
    print("[Player] 님이 게임을 퇴장하셨습니다.")

## 실제 게임 진행
game_start()

# 유닛 다수 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
r1 = Race()

# 유닛 일괄 관리 : 리스트 생성
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(r1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격모드 준비(마린: 시팀팩 모드, 탱크: 시즈모드 전환, 레이스: 클로킹 모드 전환)
for unit in attack_units:
    # 마린, 탱크, 레이스등 다양한 클래스가 있기 떄문에 다양한 클래스 인스턴스를 확인하기 위해!
    if isinstance(unit, Marine): # 파이썬의 isinstance() 함수를 이용해 각 클래스의 인스턴스를 확인
        unit.steampack()         ## 마린이 시즈모드를 할 수 없듯이 각각의 클래스에 맞는 인스턴스를 사용하기 처리를 위해 확인
    elif isinstance(unit, Tank):
        unit.set_sizmode()
    elif isinstance(unit, Race):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 피해를 랜점 수로 5~20까지의 피해

# 게임 종료
game_over()

