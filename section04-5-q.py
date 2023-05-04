 # Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("apple;orange;banana;lemon")



# 3. 화면에 * 기호 100개를 표시하세요.
print('*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
a = "300"
b = int(a)
print(type(b))
b = float(a)
print(type(b))
b = complex(a)
print(type(b))
b = str(a)
print(type(b))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
c = "Niceman"
print(c[4:])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
d= "Strawberry"

print(d[::-1])


# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
e = "010-7777-9999"
print(e.replace('-',''))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
f = "http://daum.net"
print(f[7:])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
g = "NiceMan"
print(g.upper())
print(g.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
h = "abcdefghijklmn"
print(h[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
i = list(["Banana", "Apple", "Orange"])
del i[1]
print(i)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
j = (1, 2, 3, 4)
print(type(j))
j = list(j)
print(j)
print(type(j))
print(j)

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
k = dict({"type" : ["senior", "junior", "child"], "price" : [100000, 70000, 30000]})
print(k)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
k["type"] = "baby"
k["price"] = 0

print(k)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(k.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.


# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
