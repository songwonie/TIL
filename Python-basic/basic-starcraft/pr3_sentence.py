# 문장
# sentence = "나는 소년입니다"
# sentence2 = '파이썬은 쉬워요'
# print(sentence2)


# 슬라이싱
# jumin = "910121-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0~1번째 까지
# print("월 : " + jumin[2:4]) # 2~4번째 전까지 가져옴
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
# print("뒤 7자리만 나열 : " + jumin[-7:]) # 뒤부터 출력은 뒤에서 -1번부터 -n번까지로 따짐
# print(jumin[-13:])


# 문자열처리 함수
# python = "Python is Amazing"
# print(python.lower()) # 소문자 출력
# print(python.upper()) # 대문자 출력
# print(python[0].isupper()) # isupper()는 대문자인지 아닌지 알려줌
# print(len(python)) # 문자열 길이 반환
# print(python.replace("Python", "Java")) # 특정문자를 대체

# index = python.index("n") # 특정 문자가 몇번째 있는지 값을 반환
# print(index) 
# index = python.index("n", index + 1) #특정문자 다음 위치부터 반환
# print(index)

# print(python.find("n"))
# print(python.find("Java")) # 특정문자에 Java라는 단어가 없기 때문에 이때, -1을 반환
# print(python.index("Java")) # 특정문자에 Java라는 단어가 없으면 오류라고 하며 프로그램 종료

# print(python.count("n")) # 특정문자가 몇개인지를 반환


# 문자열 포맷
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬") # %s 는 숫자든 문자든 잘표현
# print("Apple은 %c로 시작해요" % "A")
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# # python 버전 3.6이상에서 가능!나는 {age}살이며, {color}색을 좋아해요.
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")


# # 탈출 문자
# print("백문이 불여일견/n백견이 불여일타") # /n 줄을 바꿔줌

# print("저는 \"나도코딩\"입니다.")

# # \\ : 문장 내에서는 '\'  보통, 파일위치를 칠때.

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # 커서가 Red 앞으로 오고, 거기서 Pine을 쳐서 PineApple이 된다.
 
# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")


#  Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#  예) http://naver.com
#  규칙1 : http:// 부분은 제외 => naver.com
#  규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
#  규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                 (nav)               (5)            (1)          (!)
 
#  예) 생성된 비밀번호 : nav51!

# site = 'http://naver.com'
# except_text = site.replace(site[0:7], "") # site.replace("http://", "")
# except_del = except_text.replace(except_text[-4:], "") # except_text[:except_text.index(".")]  점(.) 위치 직전까지 자르기
# print(except_del)

# password = except_del[0:3] + str(except_del.count) + str(except_del.count("n")) # 오류 발생

# 최종 정답
url = 'http://naver.com'
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")] # 점(.) 직전까지!
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print(password)
print("{0} 사이트의 비밀번호는 {1} 입니다.".format(url, password))