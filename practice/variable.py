# 글로벌 함수를 사용하여 전역변수를 함수 내에 끌고와 사용하는 방법
gun = 10

def checkpoint(soldiers): 
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 지역변수를 return하여 글로벌 함수를 쓴 것과 같은 결과를 보여주는 방법
gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


# 표준체중 구하는 프로그램 작성하기
"""
 남자 : 키(m) x 키(m) x 22
 여자 : 키(m) x 키(m) x 21
 조건 1 : 표준 체중은 별도츼 함수 내에서 계산
 * 함수명 : std_weight
 * 전달값 : 키(height), 성별(gender)
 조건 2 : 표준 체중츤 소수점 둘째자리까지 표시
"""
gender = input("성별을 입력하세요. 여성/남성")
height = float(input("키를 입력하세요.(단위는 m)"))

def std_weight():
    global gender
    global height
    if gender == "여성":
        weight = height * height * 21
        print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(int(height * 100), gender, round(weight, 2)))
    else :
        weight = height * height * 22
        print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(int(height * 100), gender, round(weight, 2)))


std_weight()

def std_weight(height, gender): 
    if gender == "남성":
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm의 {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))
