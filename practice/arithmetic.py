

print('풍선')
print('침착맨'*8)

# 참 / 거짓 
print(5 > 10)
print(5 < 10)
print(not(5 > 10))

# 변수
animal = '강아지'
name = '연탄이'
age = 4
hobby = '산책'
is_adult = age >= 3

print('우리집 ' + animal + '의 이름은 ' + name + '예요.')
print(name + '는 ' + str(age) + '살이며, ' + hobby + '을 좋아해요.')
print(name + '는 어른일까요? ' + str(is_adult))



station = "신도림"


'''주석 처리는 이렇게 됩니다.
'''
print(station + "행 열차가 들어오고 있습니다.")

print(2**3) # 2^3
print(100//2) # 몫
print(100%2) # 나머지
print(100/2) # 나누기

station = '인천공항'

print(station + '행 열차가 들어오고 있습니다.')

print(1+1)
print(3-1)
print(5*2)
print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 2
print(15//3) #몫 5

print(10 > 3)
print(10 == 3)
print(10 >= 3)
print('3' == 3)

print(1 != 3)
print(not(1 != 3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)

print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number %= 2
print(number)

print(abs(-4)) #절대값
print(pow(4, 2)) # 4^2 = 16
print(max(4, 13)) 
print(min(3, 5))
print(round(3.14))

from math import *
print(floor(4.99)) # 내림
print(ceil(3.14)) # 올림
print(sqrt(16)) # 제곱근