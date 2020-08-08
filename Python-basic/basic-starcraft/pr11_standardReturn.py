# 표준입출력
# print("python", "java", sep=" vs ") #sep= 는 각 ,(콤마)사이에 들어갈 것을 지정해줌

# print("python", "java", sep=",", end="?") # end 부분은 문장이 끝나는부분에서 붙여줄 부분을 말해줌

# import sys
# print("Python", "java", file=sys.stdout) #stdout은 표준출력
# print("Python", "java", file=sys.stderr) #stderr은 표준에러 처리 

# # 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100} #딕셔너리 형태
# for subject, score in scores.items(): # items는 딕셔너리 형태에서 Key, value 동시에 출력
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust, rjust는 정렬할때 쓰이는 것

# # 은행 대기순번표
# # 001, 002, 003, ....
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #zfill은 칸의 공간을 확보하고 나머지에 0을 채워넣음


# answer = input("아무 값이나 입력하세요 : ") 
# print("입력하신 값은 " + answer + "입니다.")
# print(type(answer)) # input으로 받은 값은 항상 string으로 출력한다!


# 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) # > 오른쪽 부등호는 오른쪽 정렬

# 양수일 땐 + 로 표시, 음수일 땐 - 로 표시
print("{0: >+10}". format(500))
print("{0: >+10}". format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}". format(500))

# 3자리마다 콤마 찍어주기
print("{0:,}".format(100000000000000))

# 3자리마다 콤마 찍고, +- 부호 붙이기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

# 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니깐 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(10000000000000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점을 특정 자리수 까지만 표시하고 싶으면 (소수점 3째자리에서 반올림)
print("{0:.2f}".format(5/3))






