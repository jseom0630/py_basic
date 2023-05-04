# 파이썬 흐름제어 - 반복문
# 반복문 실습
# 코딩의 핵심 -> 조건 해결 중요
# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1
    
for v2 in range(10):
    print(v2)
    
for v3 in range(1,11):
    print("v3 is", v3)
    
a = 0    
for v4 in range(1,101):
    a = a + v4
    
print(a)
print("1~100 : ", sum(range(1, 101)))

b = 0
c = 1

while c <= 100:
    b += c
    c += 1
    
print(b)

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 딕셔너리, 집합
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ["kim", "park", "Cho", "Choi", "YOO"]

for name in names:
    print(name)

word = "debug console"

for w in word:
    print(w)
    

my_info = {
    "name" : "kim",
    "age" : 33,
    "city": "Seoul"
}

for di in my_info:
    print(di)
    
for k, v in my_info.items():
    print(k, v)   
    
for di in my_info.items():
    print(di)
    
name ="KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())
        
        
# break문
numbers = [14, 3, 4, 7, 10 ,24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print(33)
        break
    else:
        print("continue")

for num in numbers:
    if num == 33:
        print(33)
        break
    else:
        print("continue")

else:
    print("Not found...")
    
    
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입", type(v))

name = "niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))
