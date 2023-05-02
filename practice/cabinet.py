
cabinet = {3:"남건우", 100:"남희정"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) []를 쓸 경우캐비넷 키에 5가 없어서 프로그램 종료
# print(cabinet.get(5)) get을 쓸 경우 None 값을 반환하고 프로그램은 계속 실행
print(cabinet.get(5, "비어있으니 사용할 수 있습니다."))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"a-0": "남희정", "a-1": "나미"}
print(cabinet["a-0"])
print(cabinet["a-1"])

# 새 손님
print(cabinet)
cabinet["a-1"] = "김종국"
cabinet["a-2"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["a-1"]
print(cabinet)

# 키 들만 출력
print(cabinet.keys())
# 값 들만 출력
print(cabinet.values())
# 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)
