# 반복문
# for waiting in [0,1,2,3,4]:
#     print("대기번호 : {0}".format(waiting))

# for waiting in range(5): # 0,1,2,3,4
#     print("대기번호 : {0}".format(waiting))

# for waiting_num in range(1, 6): # 1,2,3,4,5
#     print("대기번호 : {0}".format(waiting_num))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer)) 


# while문, 어떤 조건이 만족할 때 까지는 반복!

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피가 매진되었습니다.")

# customer = "아이언맨"
# index = 1
# while True: # 무한 루프!
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index += 1

# 상황: 손님이 내 커피가 준비되었는지 물어볼 수 있다. 이때의 순서를 알기 위한 방법
# customer = "토르"
# person = "unknown"

# while person != customer:
#      print("{0}, 커피가 준비 되었습니다.".format(customer))
#      person = input("성함이 어떻게 되시죠? ") # 손님이 성함을 말했을때, while문에서 보다시피,
#                                             # cusutomer와 일치하지 않으면 반복문은 계속 될것이고,
#                                             # 일치하면 while문을 빠져나올 것이다.



# 한줄 for문
# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101,102,103,104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students] # 100을 붙여서 반복문
# print(students) 

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "Groot"]
# students = [len(i) for i in students] # len()을 이용하여, students의 각각의 길이를 리스트로 대입
# print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
students = [i.upper() for i in students] # upper() 대문자 변환
print(students)