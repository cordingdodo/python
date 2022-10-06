#비교 연산
a=40
b=30
c=70
print("a>b: ", a>b)
print("a>=b: ", a>=b)
print("a<b: ", a<b)
print("a<=b: ", a<=b)
print("a==b: ", a==b)
print("a!=b: ", a!=b)

#논리 연산자
#and
print("a>b && b>c : ", (a>b and b>c))
print("a<b && b<c : ", (a<b and b<c))

#or
print("a>b || b>c : ", (a>b or b>c))
print("a<b || b<c : ", (a<b or b<c))

#not 연산자
print("!(a>b) ", not(a>b))
print("!(a<b) ", not(a<b))

#비트 연산자 : &, |, ^, !, >>, <<
print("a & b: ", (a & b))
print("a | b: ", (a | b))
print("a ^ b: ", (a ^ b))
print("~a: ", ~a) #보수 #complement

#32_16_8_4_2_1
#1  0  1 0 0 0 a
#0  1  1 1 1 0 b
#0  0  1 0 0 0 and 8
#1  1  1 1 1 1 or 62
#1  1  0 1 1 0 xor 입력이 서로 다를 경우 54
#0  1  0 1 1 1 ~a : -41- > 23 - 64 결과가 나옴 보수 #complement
#1  0  0 0 0 0 -> 64-23 = (-)41
