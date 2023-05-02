
# for문 
for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["금동", "민준", "혁진", "희정", "여은"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while
customer = "희정"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 끝났습니다.")

# ctrl + c 강제종료
customer = "희정"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

absent = [2, 5] # 결석
no_book = [7] # 책을 안들고옴
for student in range(1, 11): # 1~10번까지 
    if student in absent:
        continue
    if student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와.".format(student))
        break
    print("{0}번, 책을 읽어주렴".format(student))
