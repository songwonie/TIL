# if 조건문
# 분기: 이런 상황에서는 A라는 코드를 저런 상황에서는 B라는 코드를 실행!
# weather = input("오늘 날씨는 어떄요? ") # input()은 사용자의 입력을 받는 기능
# if weather == "비" or weather == "눈": # or는 조건을 추가
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")  # 위에 있는 조건들이 모두 안맞으면 else로 출력

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요")



