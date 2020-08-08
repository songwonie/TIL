# class(클래스) : 파이썬 코딩에서 필수

# 마린 : 스타크래프트 유닛
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력: {2}]".format(\
#     name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# 그런데 탱크가 한대 더 공격하는 경우는 어떻게 해야할까? 그럼 tank2를 또 만들어야함
# 실제로 스타크래프트에서는 매우 많은 유닛이 나온다.
# 이럴때 붕어빵의 틀과 같이 클래스는 하나의 틀이라고 보면 된다.

class Unit: # 일반 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1=Unit("마린", 40, 5)
marine2=Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ (생성자) 자동호출 되는 부분
# 위에 마린과 탱크과 같이 클래스에서 생성되는 구조를 객체라고 하고, 이때 마린과 탱크는
# Unit 클래스의 인스턴스 라고 한다. 만약 마린이나 탱크를 하나의 요소만 빠진채 생성하면 
# 오류가 나타나므로, 단 하나의 요소도 빠드려서는 안된다.
# 여기서 요소는 클래스 안에 '멤버 변수'라고 부른다!

# 예시) marine2 = Unit("마린")  #에러 발생: hp와 damage 요소가 빠져있다.

# 멤버 변수 사용
# race1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(race1.name, race1.damage))

# # 외부에서 멤버변수 사용
# # 프로토스의 다크 아콘이 마인드 컨트롤을 통해 레이스 유닛을 뺻었다.
# race2 = Unit("레이스", 80, 5)
# race2.clocking = True # 파이썬은 클래스 변수외에 추가로 만들수가 있다. True를 통해
#                       # 다만 추가는 레이스2 만 추가된것이지 race1에는 추가되있지 않다.
# if race2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(race2.name))


# # 메서드(method)
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}])"\
#         .format(self.name, location, self.damage)) # 클래스에서 정의된 멤버변수는 self를 사용

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 파이어뱃
# firebat1= AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)



# 상속 : 이전의 클래스에서 멤버변수를 상속받는 것

class noAttackUnit: #메딕과 같이 공격이 없는 유닛
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    
class AttackUnit(noAttackUnit): # 공격력이 없는 유닛에서 name과 hp를 상속받음
    def __init__(self, name, hp, damage):
        noAttackUnit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}])"\
        .format(self.name, location, self.damage)) # 클래스에서 정의된 멤버변수는 self를 사용

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃
firebat1= AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 다중 상속 (부모가 둘 이상으로 여러 개의 클래스로부터 상속을 받는 기능!)
# 드랍쉽: 공중 유닛, 수송 기능
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
        .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 = 공격유닛 클래스 + 공중유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage) # 공격유닛 초기화
        Flyable.__init__(self, flying_speed) # 공중유닛 초기화

# 발키리: 강력한 공중유닛
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") # Flyable 경우 name 멤버변수는 따로 없기 때문에 .name을 준다








        