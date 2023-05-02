
print("Python", "Java", sep=", ")
print("Python", "Java", "Javascript", sep=" vs ")
print("Python", "Java", "Javascript", sep=", ", end="! ")
print("무엇이 제일 재밌을까요?")

import sys
print("Python", "Java", "Javascript", file=sys.stdout)
print("Python", "Java", "Javascript", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":80, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(3), str(score).rjust(4), sep=":") # 칸 확보 밑 왼쪽 오른쪽 정렬

# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ") # input으로 받으면 무조건 str 타입임
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되 총 10자리를 확보
print("{0: >10}".format(500))
# 양수 일때는 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
print("{0:+,}".format(1000000000))
print("{0:+,}".format(-1000000000))
print("{0:!<+30,}".format(1000000000))
# 소수점 출력
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3)) # 소수점 3째자리에서 반올림
