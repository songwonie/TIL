# continue와 break, 반복문 내에서 쓸수 있는것
# absent = [2, 5] # 결석한 학생
# no_book = [7] # 책을 안져온 학생

# for student in range(1, 11): # 1~10번 까지 학생
#     if student in absent: 
#         continue # 지정학생이 결석했다면 반복문 계속
#     elif student in no_book:
#         print("오늘 수업 여기까지! {0}은 교무실로 따라와!!".format(student))
#         break # 특정학생이 반복문 중에 걸리면 프로그램 종료!
#     print("{0} 학생, 일어나서 책을 읽어봐.".format(student))



# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만을 매칭해야 합니다.
# 조건3 : (내가 임의로 추가함) 탑승 승객이 10명이 되면 매칭을 종료한다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# 나의 답안
# from random import *

# rand_time = randint(5, 51)
# maching = range(5, 16)
# maching = list(maching)
# # print(rand_time)
# # print(maching)

# for customer in range(1, 51):
#     print("{0}번째 손님 (소요시간 : {1}분".format(customer, rand_time))
#     if rand_time <= 15:


# 모범 답안 
from random import *

cnt = 0  # 5~15분 소요시간 탑승 승객의 숫자를 구하므로, 탑승 승객수 초기화
for i in range(1, 51):
    time = randrange(5, 51) # 소요시간
    if 5 <= time <= 15: # 매칭 성공
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1 # 탑승 승객 추가
        if cnt == 10: # 추가, 탑승승객이 10명이 되면 종료
            break
    else: # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}명 완료".format(cnt))