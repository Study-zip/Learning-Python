
# 집합(set) 중복 안됨, 순서 없음
my_set = {1,2,3,4,5,6,2,3,1}
print(my_set)

java = {"유재석", "조세호", "침착맨"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가
python.add("김태호")
print(python)

# 제거
python.remove("김태호")
print(python)
