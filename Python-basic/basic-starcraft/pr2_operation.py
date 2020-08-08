# 기본연산
# print(2**3)
# print(5 % 3)  # 나머지
# print(10//3)  # 몫

# print(4 >= 7) # false
# print(3 == 3) # true
# print(2 == 4) # false
# print(3 + 4 == 7) # true

# print(1 != 3) # 같지 않다

# print((3 > 0) & (3< 5)) # and 의미
# print((3 > 0) or (3 > 5))
# print((3 > 0)) | (3 > 5)) # or 의미

# print(5 > 4 > 3) # True

# number = 2 + 3 * 4 # 14
# number /= 2 # 나누기 2
# print(number)
# number -= 2

# 숫자처리 함수
# print(abs(-5))  # 절대값
# print(pow(4, 2)) # 4의 2승 = 16
# print(max(4, 5)) # 최대값 최소값은 min
# print(round(3.15)) # 반올림 3.2
# from math import *
# print(floor(4.99)) # 소수점 내림 4, math 임포트필요
# print(sqrt(16)) # 제곱근 4, math 임포트필요

# 랜덤함수
# from random import *
# print(random()) # 0.0~1.0 미만의 임의값 생성
# print(random() * 10) # 0.0~10.0 미만의 임의값 생성
# print(int(random() * 10)) # 0~10 미만의 임의값 생성
# print(int(random() * 10) + 1) # 1~10 이하의 임의값 생성

# # 로또 숫자를 임의로 생성해보자 (로또 숫자는 1부터 45까지)
# print(int(random() * 45) + 1) # 1~45 이하의 임의의 값을 생성
# print(randrange(1, 46)) # 1~46미만의 숫자를 임의값으로 생성
# print(randint(1, 45)) # 1~45이하의 임의의 값을 생성


# # Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1: 랜덤으로 날짜를 뽑아야 함
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 x 일로 선정되었습니다.
from random import *

offline_1 = randint(4, 28)
offline_2 = int((random()*29) + 4) # 4~29미만의 임의의 값 생성
offline_3 = int(randrange(4, 29)) # 4~29미만의 임의의 값 생성

print("오프라인 스터디 모임 날짜는" + str(offline_2) + "일로 선정되었습니다.") 