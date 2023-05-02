
sentence = '나는 남희정입니다.'
print(sentence)
sentence2 = "나는 나미입니다."
print(sentence2)
sentence3 = """
나는 남희정이고
나미라고 부르세요.
"""
print(sentence3)

jumin = "960216-2234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4]) # 2-3
print("일 : " + jumin[4:6]) # 4-5
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤부터) : " + jumin[-7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # 대문자 확인
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java")) # 값 바꾸기

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 찾는 게 없을 경우 -1 반환
# print(python.index("Java")) # 찾는 게 없을 경우 오류 반환 (종료 시켜버림)
print(python.count("n"))

print("a"+"b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." %28) # d는 정수값 
print("나는 %s을 좋아해요." %"파이썬") # s string
print("Apple은 %c로 시작해요." %"A") # Character 문자 1개
print("나는 %s색과 %s색을 좋아해요." %("파란", "노란"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "노란"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "노란"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "노란"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 28, color = "초록"))

# 방법 4 (v3.6 이상~)
age = 29
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

print("백문이 불여일견\n백견이 불여일타") # \n 줄바꿈 
print("저는 '남희정'입니다.") # 큰 따옴표 내 작은 따옴표 가능
print("저는 \"남희정\"입니다.") # \"문자\" 혹은 \'문자\'로 따옴표 내 따옴표 사용가능

# \\ : 문장 내에서 \
print("\\Usr\\bin")
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")

# 비밀번호 생성하기
url = "http://youtube.com"
my_str = url.replace("http://","") 
my_str = my_str[:my_str.index(".")] # my_str[0:5] 0~5 직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))
