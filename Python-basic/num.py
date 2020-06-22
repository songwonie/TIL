'''짝수/홀수 구분하기'''

# 1) str형 구분
num_str = input("숫자를 입력하시오:")
last_str = num_str[-1]
print(type(last_str))

if last_str in '02468':
	print("짝수")
elif last_str in '13579':
	print("홀수)

# 2) int형 구분
str = input("숫자를 입력하시오:")
num = int(str) # int형 변환
print(type(num))

if num % 2 == 0:
	print("짝수")
if num % 2 == 1:
	print("홀수")