# dictionary
# cabinet = {3:"유재석", 100:"조세호"} # Key:Value 값을 지님

# print(cabinet[3]) # 3번에는 유재석이 출력
# print(cabinet.get(3))
# print(cabinet[5]) # 5라는 key가 없기 때문에 프로그램 종료
# print(cabinet.get(5)) # get은 None을 출력
# print(cabinet.get(5, "사용 가능")) # 5번이라는 key를 가져오고 없으면 "사용가능" 값을 가져옴
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False 출력

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # 유재석과 key가 같으므로 이떄는, 김종국이 값으로 들어감
cabinet["C-20"] = "조세호" # 조세호 값을 지니는 key value 추가
print(cabinet)

# 간 손님, dictionary key 삭제
del cabinet["A-3"]

# Key들만 출력
print(cabinet.keys()) 

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점, dictiondary 삭제
cabinet.clear()
print(cabinet)

