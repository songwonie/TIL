# 튜플 : 리스트와는 다르게 내용 추가나 변경할수 없지만 속도가 빠르다.
#        변경되지 않는 목록을 사용할 때 이용
# menu = ("돈까스", "치즈까스")

# 메뉴 추가
# menu.add("생선까스") # 튜플은 추가가 안됨! 오류

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩") # 튜플은 한번에 선언이 가능!
# print(name, age, hobby)


# 세트 (set) 집합
# 중복 안됨, 순서는 보장되지 않음!!
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합, java와 python을 모두할 수 있는 사람
# print(java & python)
# print(java.intersection(python))

# # 합집합, java 할수 있거나 python도 할수 있는 사람
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할수 있지만 python은 할 줄 모르는 사람)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남, 세트 추가
# python.add("김태호")
# print(python)

# # Java를 까먹었어요, 차집합, 값 뺴기
# java.remove("김태호")
# print(java)


# # 자료구조의 변경
# # 커피숍
# menu = {"커피", "우유", "주스"} # set 형태
# print(menu, type(menu))

# menu = list(menu) # set 형태를 list형으로 변형!
# print(menu, type(menu))

# menu = tuple(menu) # tuple 형으로 변형
# print(menu, type(menu))

# menu = set(menu) # 다시 set형으로 변형


# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample을 활용

# (출력예제)
#   -- 당첨자 발표 --
#   치킨 당첨자 : 1
#   커피 당첨자 : [2, 3, 4]
#   -- 축하합니다 --

# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst) # shuffle은 리스트의 값을 무작위로 바꿔줌
# print(lst)
# print(sample(lst, 1)) # sample은 무작위로 1개를 뽑는다.

# 나의 답안
# from random import *
# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(id)
# # print(id)
# chicken = sample(id, 1)

# id = set(id)
# chicken = set(chicken)
# # print(type(chicken))

# id = id - chicken
# # print(chicken)
# # print(id, type(id)) 
# coffee = sample(id, 3)
# # print(coffee)

# chicken = list(chicken)
# coffee = list(coffee)
# print(chicken)
# print(coffee)

# print("   -- 당첨자 발표 --   \n")
# print("   치킨 당첨자 : %d" % chicken[0])
# print("   커피 당첨자 : %d, %d, %d" % coffee[0], coffee[1], coffee[2])
# print("   -- 축하합니다 --    ")


# 모범 답안
from random import *
users = range(1, 21) # 1부터 20까지의 숫자를 생성
# print(type(users)) # type이 range라고 나오며, range는 리스트 형태가 아님!
users = list(users)
# print(type(users)) 

# print(users)
# shuffle(users)
# print(users)

winners = sample(users, 4)  # 중복을 피하기 위해, 우선 4명을 뽑는다.
                            # 나의 경우는 1명 뽑고, set형으로 바꾼다음에 1명을 뺀 나머지에서 3명을 뽑았다.
                       
print("   -- 당첨자 발표 --   \n")
print("   치킨 당첨자 : {0}".format(winners[0]))
print("   커피 당첨자 : {0}".format(winners[1:])) # 0번째를 뽑았으니 1부터 끝까지!
print("   -- 축하합니다 --    ")