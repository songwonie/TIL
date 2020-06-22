'''temp 변수 활용, swap function 만들기'''

a, b = input("두 개의 문장을 입력하시오: ").split()
print(a, b)

def swap(a, b):
	temp = a  #a값 임시저장
	a = b
	b = temp
	return a, b

swap(a, b)