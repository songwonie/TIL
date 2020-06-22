'''여러 개의 int형의 입력값 받기 (map( ) 이용)'''

# 여러 개의 입력값을 int형 처리 
a, b, c, d = map(int, input("정수를 입력하시오: ").split())

# 기본
e, f = input("정수를 입력하시오: ").split()

print(type(a)) # int형
print(type(f)) # str형
print(a + d)
print(e + f) # 전혀 다른 연산결과.

# 값 크기비교
if a > b:
	print(a)
elif a < b:
	print(b)