# 파이썬 데이터 타입(자료형)
# Dictionary, 집합 자료형
# Dict : 순서/중복 X, 수정/삭제 O
# Key, Value 형식 -> json 형식 / mongoDB 등

#선언
a = {'name':'Eom', 'phone':'010-1111-1111','birth':860630}
b = {0:'hello', 1:'hi'} 
c = {'arr':[1, 2, 3, 4, 5]}


print(type(a))
print(a['name'])
print(a.get('name'))
print(a.get('address'))
print(c['arr'][1:3])

a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1,2,3)
print(a)

# keys, values, items

print(a.keys()) # print(a.keys()[2]) 불가
print(list(a.keys()))

print(a.values())
print(list(a.values())[1:3])

print(a.items())

print(2 in b)
print('name2' in a)
print('name2' not in a)

# 집합 Sets (순서/중복 X, 수정/삭제 O)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6 ,7 ,8 ,9])
print(s1.intersection(s2))
print(s1 & s2)

print(s1 | s2)
print(s1.union(s2))

print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
s3.add(7)
print(s3)
s3.remove(15)
print(s3)
