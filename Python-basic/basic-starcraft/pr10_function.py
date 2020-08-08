# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0) 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금 수수료
    commission = 100 #수수료 100원
    return commission, balance - money - commission  # 여러개의 값을 return할수 있다


balance = 0 # 잔액
balance = deposit(balance, 1000) # 1000원 입금
print(balance)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


# 함수에서 기본값을 설정하는 방법
# def profile(name, age, main_lang):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#     .format(name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("조세호", 25, "자바")

# 같은 학교 같은 학년 같은 반
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#     .format(name, age, main_lang))

# profile("유재석")
# profile("조세호")


# 키워드값을 이용한 함수 호출
# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="조세호")  #key가 뒤섞여있어도 제기능을 발휘


# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: : {0}\t".format(name, age), end=" ") # end=" " 다음 함수를 이어서 한줄에 출력해줌
#     print(lang1, lang2, lang3, lang4, lang5)

#     profile("유재석", 20, "python", "java", "c", "c++") # 매번 인자를 넣어줘야하는 번거로움 때문에 가변인자를 넣어야한다

# 가변인자 사용예시
def profile(name, age, *language):
    print("이름: {0}\t, 나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c++", "kotlin")
profile("조세호", 25, "kotlin", "swift")


# 지역변수와 전역변수
gun = 10 # 전역변수

def checkpoint(soldiers): #경계근무
    global gun # 전역공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))

gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))



# Quiz) 표준 체중을 구하는 프로그램을 작성하시오
# * 표준체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#             * 함수명 : std_weight
#             * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.


def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender), 2) #return 값을 받기 위해서 변수넣음, cm단위 m단위로 변환
                                                  #round()를 통해 소수점 둘째자리까지 표시
print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, weight))                             
    

