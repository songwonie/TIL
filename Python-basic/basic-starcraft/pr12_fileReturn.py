# 파일 입출력
# 파일 열기
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학: 0", file=score_file)
# print("영어: 0", file=score_file)
# score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # "a"는 기존의 있는 파일에서 내용추가!
score_file.write("과학 : 80")
score_file.write("\n코딩 ; 100")

# 파일 읽어오기
score_file = open("score.txt", "r", encoding="utf8") 
print(score_file.readline()) #줄별로 읽기, 한줄 읽고 다음줄로 이동
print(score_file.readline(), end="") #다음줄로 넘어가기 싫으면
score_file.close()


# 한줄씩 읽어오되, 내용이 없으면 종료
score_file = open("score.txt", "r", encoding="utf8") 
# while True: # 파일의 내용이 몇줄인지 모를떄는 무한 반복문을 통해서 몇줄인지 읽어올수 있다.
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

lines = score_file.readlines() # 모든 line을 가지고 와서 list 형태로 저장!
for line in lines:
    print(line, end="") 

score_file.close()


# 피클
import pickle
# profile_file = open("profile.pickle", "wb") # "wb"에서 b는 binary를 의미하는데 pickle해올땐 항상 바이너리 타입으로 지정 필요!
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프"]}
# pickle.dump(profile, profile_file) # 위에 정의한 profile 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # 읽어오기
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# with 파일입출력 : 파일입출력을 단 한줄만으로 작성이 가능하고, close할 필요가 없다.
import pickle

with open("profile.pickle", "rb") as profile_file: #피클 파일의 내용 읽어오기
    print(pickle.load(profile_file)) # close 할필요 없다.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부중")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



# Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

#  - x 주차 주간보고 -
#  부서 : 
#  이름 :
#  업무 요약 :

#  1주차부터 50주차까지 보고서 파일을 만드는 프로그램을 작성하시오.

#  조건 : 파일명은 '1주차.txt', '2주차.txt', .... 와 같이 만듭니다.

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("부서 : ")
        report_file.write("이름 : ")
        report_file.write("업무 요약 : ")




