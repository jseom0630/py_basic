#문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = "NiceMan"
str3 = ''
str4 = ' '
str5 = str()
str6 = str('')
print(len(str1), len(str2), len(str3), len(str4), len(str5), len(str6))


escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab \t"
print(escape_str2)
 
 # Raw String
 # raw_s1 = r'/Users/jseom'

# 멀티라인
multi = \
"""문자열 
멀티라인 
테스트"""

print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_o4 = "nice man"
print(str_o1 * 100)
print(str_o2 + str_o3)
# print(str_o1 +3) 자료형이 달라서 에러 발생
print('a' in str_o4)
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환

print(type(str(77)))
print(str(10.4))


# 문자열 함수
a = "niceman"
b = "orange"
print(a.islower())
print(a.endswith('s'))
print(b.endswith('e'))
print(a.capitalize())
print(a.replace('nice','bad'))
print(list(reversed(b)))

#슬라이싱
c = "niceman"
d = "orange"
print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:len(a)])
print(a[0:len(a)-1])
print(a[:4])
print(a[:])
print(a[0:])
print(b[0:4:2])
print(b[1:-2])
print(b[::-1])