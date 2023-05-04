# Section02-1
# 파이썬 기초 코딩
#print 구문의 이해

# 기본출력

print('Hello Python!')
print("hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()


# Separator 옵션 사용
print('T','E','S','T', sep='')
print('2019','02','19', sep='-')

# end 옵션 사용
print('Welcome To ', end='')
print('the black paradaise', end=' ')
print('piano notes')
print('test')

print()

# format사용
print('{} and {}'.format('You','I'))
print("{0} and {1} and {0}".format('you','I'))
print("{a} are {b}".format(a='You', b='I'))
print("%s's favorite number is %d" %('Test', 7)) #%s : string, %d : 정수, %f : float

print()

print("test1: %5d, price: %4.2f" %(776, 6543.123))
print("Test1: {0:5d}, Price: {1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123))
print("Test1: {0: 5d}, Price:{b: 4.2f}".format(776, b=6534.123))
print("Test1: %5d, Price: {0: 4.2f}, test : {a}".format(1234.567, a='test') %(123))
# print("Test1: %5d, Price: {0: 4.2f}, test : {a}" %(123).format(1234.567, a='test'))  < 에러 발생


# Escape 코드
print()
print()
#print(''you'') < error

'''
\n 개행
\t 탭
\\
\'
\"
\r 캐리지 리턴
\f : vha vlem
\a : 벨 소리
\b : 백스페이스
\000 : 널 문자
'''
