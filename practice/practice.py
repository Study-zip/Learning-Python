#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import numbers
import os, sys
from turtle import heading


# print('풍선')
# print('침착맨'*8)

# 참 / 거짓 
# print(5 > 10)
# print(5 < 10)
# print(not(5 > 10))

# 변수
# animal = '강아지'
# name = '연탄이'
# age = 4
# hobby = '산책'
# is_adult = age >= 3

# print('우리집 ' + animal + '의 이름은 ' + name + '예요.')
# print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 좋아해요.')
# print(name + '는 어른일까요? ' + str(is_adult))



# station = "신도림"


'''주석 처리는 이렇게 됩니다.
'''
# print(station + "행 열차가 들어오고 있습니다.")

# print(2**3) # 2^3
# print(100//2) # 몫
# print(100%2) # 나머지
# print(100/2) # 나누기

# station = '인천공항'

# print(station + '행 열차가 들어오고 있습니다.')

# print(1+1)
# print(3-1)
# print(5*2)
# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(15//3) #몫 5

# print(10 > 3)
# print(10 == 3)
# print(10 >= 3)
# print('3' == 3)

# print(1 != 3)
# print(not(1 != 3))
# print((3 > 0) and (3 < 5))
# print((3 > 0) & (3 < 5))
# print((3 > 0) or (3 < 5))
# print((3 > 0) | (3 < 5))

# print(5 > 4 > 3)

# print(2 + 3 * 4)
# print((2 + 3) * 4)
# number = 2 + 3 * 4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number %= 2
# print(number)

# print(abs(-4)) #절대값
# print(pow(4, 2)) # 4^2 = 16
# print(max(4, 13)) 
# print(min(3, 5))
# print(round(3.14))

# from math import *
# print(floor(4.99)) # 내림
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근

# from random import *

# print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 이상 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 이상 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) # 1~ 10 이하의 임의의 값 생성
# print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# date =  randint(4, 28)
# print('오프라인 스터디 모임 날짜는 매월 ' + str(date) + '일로 선정되었습니다.')

# sentence = '나는 남희정입니다.'
# print(sentence)
# sentence2 = "나는 나미입니다."
# print(sentence2)
# sentence3 = """
# 나는 남희정이고
# 나미라고 부르세요 그냥.
# """
# print(sentence3)

# jumin = "960216-2234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
# print("월 : " + jumin[2:4]) # 2-3
# print("일 : " + jumin[4:6]) # 4-5
# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리(뒤부터) : " + jumin[-7:])

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) # 대문자 확인
# print(len(python)) # 문자열 길이
# print(python.replace("Python", "Java")) # 값 바꾸기

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("Java")) # 찾는 게 없을 경우 -1 반환
# # print(python.index("Java")) # 찾는 게 없을 경우 오류 반환 (종료 시켜버림)
# print(python.count("n"))

# print("a"+"b")
# print("a", "b")

# 방법 1
# print("나는 %d살입니다." %28) # d는 정수값 
# print("나는 %s을 좋아해요." %"파이썬") # s string
# print("Apple은 %c로 시작해요." %"A") # Character 문자 1개
# print("나는 %s색과 %s색을 좋아해요." %("파란", "노란"))

# # 방법 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "노란"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "노란"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "노란"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 28, color = "초록"))

# 방법 4 (v3.6 이상~)
# age = 29
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문이 불여일견\n백견이 불여일타") # \n 줄바꿈 
# print("저는 '남희정'입니다.") # 큰 따옴표 내 작은 따옴표 가능
# print("저는 \"남희정\"입니다.") # \"문자\" 혹은 \'문자\'로 따옴표 내 따옴표 사용가능

# # \\ : 문장 내에서 \
# print("\\Usr\\bin")
# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# # \b : 백스페이스(한 글자 삭제)
# print("Redd\bApple")
# # \t : 탭
# print("Red\tApple")

# 비밀번호 생성하기
# url = "http://youtube.com"
# my_str = url.replace("http://","") 
# my_str = my_str[:my_str.index(".")] # my_str[0:5] 0~5 직전까지
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 리스트
# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway.index("조세호"))
# subway.append("하하")
# print(subway)
# subway.insert(1, "정형돈")
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]

# num_list.extend(mix_list)
# print(num_list)

# cabinet = {3:"남건우", 100:"남희정"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5]) []를 쓸 경우캐비넷 키에 5가 없어서 프로그램 종료
# # print(cabinet.get(5)) get을 쓸 경우 None 값을 반환하고 프로그램은 계속 실행
# print(cabinet.get(5, "비어있으니 사용할 수 있습니다."))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"a-0": "남희정", "a-1": "나미"}
# print(cabinet["a-0"])
# print(cabinet["a-1"])

# # 새 손님
# print(cabinet)
# cabinet["a-1"] = "김종국"
# cabinet["a-2"] = "조세호"
# print(cabinet)

# # 간 손님
# del cabinet["a-1"]
# print(cabinet)

# # 키 들만 출력
# print(cabinet.keys())
# # 값 들만 출력
# print(cabinet.values())
# # 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스") 튜플은 값이 변경될 수 없음.

# name = "김종국"
# age = 28
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 28, "코딩")
# print(name, age, hobby)

# 집합(set) 중복 안됨, 순서 없음
# my_set = {1,2,3,4,5,6,2,3,1}
# print(my_set)

# java = {"유재석", "조세호", "침착맨"}
# python = set(["유재석", "박명수"])

# # 교집합
# print(java & python)
# print(java.intersection(python))

# # 합집합
# print(java | python)
# print(java.union(python))

# # 차집합
# print(java - python)
# print(java.difference(python))

# # 추가
# python.add("김태호")
# print(python)

# # 제거
# python.remove("김태호")
# print(python)

# 자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))

# 활용 예제
# from random import *
# Lst = [1,2,3,4,5]
# print(Lst)
# shuffle(Lst)
# print(Lst)
# print(sample(Lst, 1))

# from random import *
# event = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(event)
# ingan = sample(event, 4)

# print("""
# -- 당첨자 발표 --
# 치킨 당첨자 : {0}
# 커피 당첨자 : {1}
# -- 축하합니다 --
# """.format(ingan[0], ingan[1:]))
# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
# users = list(users)
# print(type(users))
# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4) 
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

# 분기
# weather = input("오늘 날씨는 어때요? ")

# if weather == "비":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더우니, 외출을 삼가하세요.")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요. 나갑시다!")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

# for문 
# for waiting_no in range(5):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["금동", "민준", "혁진", "희정", "여은"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# while
# customer = "희정"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 끝났습니다.")

# ctrl + c 강제종료
# customer = "희정"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# absent = [2, 5] # 결석
# no_book = [7] # 책을 안들고옴
# for student in range(1, 11): # 1~10번까지 
#     if student in absent:
#         continue
#     if student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
#         break
#     print("{0}번, 책을 읽어주렴".format(student))

# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# 학생이름을 길이로 변환
# students = ["나미", "나미정나미", "남이섬", "남희즈미", "감자도리도리"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["nami", "namhuijeong", "potato"]
# students = [i.upper() for i in students]
# print(students)

'''
당신은 카카오 서비스를 이용하는 택시 기사님 입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야됩니다.
'''
# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 4 < time < 16 :
#         cnt += 1
#         check = "O"
#     else: check = " "
#     print("[{0}]{1}번째 손님 (소요시간 : {2}분)".format(check, i, time))
# print("총 탑승 승객 : {0}분".format(cnt))

# 정답
# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
#     time = randrange(5, 51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: 
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {0}분".format(cnt))

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("이름 :{0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("남희정", 28, "자바스크립트")

# 같은 학교 같은 학년 같은 반 같은 수업 = 기본값 설정하기

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 :{0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("유재석")
# profile("남희정", 28, "자바스크립트")
# profile("김태호", 23)

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", name="김태호", age=21)

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 :{0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 :{0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("남희정", 28, "Python", "C++", "C", "Java", "Javascript", "TypeScript")
# profile("김태호", 24, "Kotlin", "Swift")

# 글로벌 함수를 사용하여 전역변수를 함수 내에 끌고와 사용하는 방법
# gun = 10

# def checkpoint(soldiers): 
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# 지역변수를 return하여 글로벌 함수를 쓴 것과 같은 결과를 보여주는 방법
# gun = 10

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# 표준체중 구하는 프로그램 작성하기
"""
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21
 조건 1 : 표준 체중은 별도츼 함수 내에서 계산
 * 함수명 : std_weight
 * 전달값 : 키(height), 성별(gender)
 조건 2 : 표준 체중츤 소수점 둘째자리까지 표시
"""
# gender = input("성별을 입력하세요. 여성/남성")
# height = float(input("키를 입력하세요.(단위는 m)"))

# def std_weight():
#     global gender
#     global height
#     if gender == "여성":
#         weight = height * height * 21
#         print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(int(height * 100), gender, round(weight, 2)))
#     else :
#         weight = height * height * 22
#         print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(int(height * 100), gender, round(weight, 2)))


# std_weight()

# def std_weight(height, gender): 
#     if gender == "남성":
#         return height * height * 22
#     else :
#         return height * height * 21

# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm의 {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

# print("Python", "Java", sep=", ")
# print("Python", "Java", "Javascript", sep=" vs ")
# print("Python", "Java", "Javascript", sep=", ", end="! ")
# print("무엇이 제일 재밌을까요?")

# import sys
# print("Python", "Java", "Javascript", file=sys.stdout)
# print("Python", "Java", "Javascript", file=sys.stderr)

# 시험 성적
# scores = {"수학":0, "영어":80, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(3), str(score).rjust(4), sep=":") # 칸 확보 밑 왼쪽 오른쪽 정렬

# 은행 대기 순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ") # input으로 받으면 무조건 str 타입임
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

#빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되 총 10자리를 확보
# print("{0: >10}".format(500))
#양수 일때는 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# 왼쪽 정렬하고 빈칸을 _로 채움
# print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000))
# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))
# print("{0:!<+30,}".format(1000000000))
# 소수점 출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3)) # 소수점 3째자리에서 반올림

# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # append
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름" : "남희정", "나이" : 28, "취미" : ["영화 감상", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 잇는 정보를 파일에 저장.
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# close를 쓸 필요 없음

# with open("study.txt", 'w', encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있습니다.")

# with open("study.txt", "r", encoding='utf8') as study_file:
#     print(study_file.read())


# for week in range(1, 51):
#     weekreport = open("{0}주차.txt".format(week), "w", encoding="utf8")
#     weekreport.write("""
#     - {0}주차 주간보고 -
#     부서 : 
#     이름 :
#     업무 요약 :
#     """.format(week))
#     weekreport.close()


# for week in range(1, 51):
#     with open(str(week)+ "주차.txt", "w", encoding="utf8") as weekreport:
#         weekreport.write("- {0}주차 주간보고 -".format(week))
#         weekreport.write("\n부서 : ")
#         weekreport.write("\n이름 : ")
#         weekreport.write("\n업무 요약 : ")

# A, B = map(int, input().split())

# print(A+B)
# print(A-B)
# print(A*B)
# print(A/B)
# print(A%B)

# year = int(input())

# if (year % 4 == 0) & (year % 100 != 0) | (year % 400 == 0):
#     print("1")
# else :
#     print("0")

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음.
# name = "마린"
# hp = 40 # 유닛의 체력
# damage = 5 #유닛의 공격력

# print("{0}유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0}유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염 방사기. 
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송, 공격 X
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# # 메소드 오버라이딩
# battlecruiser.move("9시")

# 건물