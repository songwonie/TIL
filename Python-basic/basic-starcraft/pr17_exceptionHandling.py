# # 예외 처리
# # 나누기 전용 계산기
# try:
#     print("나누기 전용 계산시입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력했습니다.")

# ## try문 내에서 정상적으로 작동하다가 무엇인가 오류 문제가 발생이 되면,
# ## except 부분이 실행될 수 있다.

# except ZeroDivisionError as err:
#     print(err)

# ## ZeroDivisionError를 통해 에러문을 나타낼수도 있음!

# except Exception as err:
#     print("알 수 없는 에러발생!!")
#     print(err)

# ## ValueError와 ZeroDivisionError 문에서도 발생하지 않은 에러는 밑에 except에서 발생!



# # 에러 발생시키기(의도적으로 에러발생)
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10: # 첫/두번째 값이 10보다 같거나 크면,
#         raise ValueError         # 에러 발생!

# except ValueError:
#     print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요!")



# # 사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, message):
#         self.message = message
    
#     def __str__(self):
#         return self.message

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10: # 첫/두번째 값이 10보다 같거나 크면,
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))    
#          # 사용자 정의 에러! format으로 지정한 입력값을 위에 class에 message로 던진다.

# except ValueError:
#     print("잘못된 값을 입력했습니다. 한자리 숫자만 입력하세요!")
# except BigNumberError as err:
#     print("에러 발생! 한자리 숫자만 입력하세요!")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# 예외처리 구문 중에서는 finally가 있는데, 에러가 발생해도 무조건 출력해준다.

## 이러한 예외처리 구문이 의미가 있는 것은 프로그래머가 꺼내려는 파일이 없거나,
## 또는 입력한 리스트에 해당 내용이 없을때, 프로그램의 종료를 막고 에러 부분이 
## 무엇인지를 알려준다. 



# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
#         대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 
#         제작하였습니다. 시스템 코드를 확인하고 적절한 예외처리 구문을
#         넣으시오.

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 떄는 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#         치킨 소진시 사용자 정의 에러(SoldOutError)를 발생 시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]
chicken = 10
waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작

# 문제 
# while(True):
#     print("[남은 치킨 : {0}]".format(chicken))
#     order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#     if order > chicken: # 남은 치킨보다 주문량이 많을 때
#         print("재료가 부족합니다.")
#     else:
#         print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#         .format(waiting, order))
#         waiting += 1
#         chicken -= order

# 풀이(5:10:07)
while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken: # 남은 치킨보다 주문량이 많을 때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
            .format(waiting, order))
            waiting += 1
            chicken -= order
    except ValueError 

    

 
