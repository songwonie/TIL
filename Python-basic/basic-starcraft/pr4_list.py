# 리스트 [] : 순서를 가지는 객체의 집합
subway = ["유재석", "박명수", "조세호"]

# 조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐, 리스트 추가
subway.append("하하")

# 정형돈을 유재석과 박명수 사이에 태움, 넣어줄 리스트 순서와 넣어줄 이름 적기
subway.insert(1, "정형돈")

# 지하철에 있는 사람을 한명씩 꺼냄
print(subway.pop()) # 맨뒤에 하하가 빠짐
print(subway)

# 같은 이름의 사람이 몇명있는지 확인하기
subway.append("유재석")
print(subway.count("유재석"))

# 정렬도 가능()
num_list= [5,2,4,3,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()

# 리스트의 값을 모두 지움
# num_list.clear()

# 다양한 자료형 함께 사용할 수 있다.
mix_list = ["조세호", 20, True]

# 리스트 확장, 하나의 리스트로 합치는 것도 가능
num_list.extend(mix_list)
print(num_list)