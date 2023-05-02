
# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

# 활용 예제
from random import *
Lst = [1,2,3,4,5]
print(Lst)
shuffle(Lst)
print(Lst)
print(sample(Lst, 1))

from random import *
event = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
shuffle(event)
ingan = sample(event, 4)

print("""
-- 당첨자 발표 --
치킨 당첨자 : {0}
커피 당첨자 : {1}
-- 축하합니다 --
""".format(ingan[0], ingan[1:]))
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
print(type(users))
users = list(users)
print(type(users))
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) 
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생이름을 길이로 변환
students = ["나미", "나미정나미", "남이섬", "남희즈미", "감자도리도리"]
print(students)
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["nami", "namhuijeong", "potato"]
students = [i.upper() for i in students]
print(students)