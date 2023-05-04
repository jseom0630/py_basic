# Section02-2
# 파이썬 기초 코딩 / 몸풀기 코딩 실습

# import this 
import sys

# 파이썬 기본 인코딩

print(sys.stdin.encoding)  # <<UTF8
print(sys.stdout.encoding)   # UTF8

# 출력문
print('My name is Jaesik!')

# 변수 선언
myName = 'jaesik'
print(myName)

# 조건문
if myName == "jaesik":
    print('OK')
    
    
# 반복문
for i in range(1, 10):
    for j in range(1,10):
        print('%d * %d =' %(i, j), i*j)
        
# 변수선언 _ 한글
이름 = "재식" # 한글은 권장되지 않음 / 자유도가 높은 언어
print(이름)

# 함수 선언

def 인사():
    print("안녕하세요")
    
인사()

def greeting():
    print('hello')

greeting()


# Class

class Cookie:
    pass

# 클래스 객체 생성

cookie = Cookie()

print(id(cookie))
print(dir(cookie))