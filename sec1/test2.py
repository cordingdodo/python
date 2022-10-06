#파이썬은 선언과 동시에 초기화
#데이터 입력 : input(입력메세지)
#캐스팅(casting) : 형 변환
su1 = int(input("숫자 1 입력 : ")) #정수로 형변환이 필요
su2 = int(input("숫자 2 입력 : ")) #

print("결과 :", su1+su2)

#정수로 형변환
a="100"
b=6.28
c=True #숫자로 형변환  True:1, False:0
d=int(a) #a="100", d=100
e="kim1004" #숫자 형태로 형변환 불가
print("a를 정수로 형변환: ", type(a), int(a), type(int(a)))
print("b를 정수로 형변환: ", type(b), int(b), type(int(b)))
print("c를 정수로 형변환: ", type(c), int(c), type(int(c)))
print("d를 정수로 형변환: ", type(d), int(d), type(int(d)))

print("*******************")

#실수로 형변환
a1="62.34"
a2=90
a3=False
print("a를 실수로 형변환: ", type(a1), float(a1), type(float(a1)))
print("b를 실수로 형변환: ", type(a2), float(a2), type(float(a2)))
print("c를 실수로 형변환: ", type(a3), float(a3), type(float(a3)))

print("*******************")
#논리로 형변환
#값이 없거나 0인 경우만 False로 나옴
b1="False"
b2=1004
b3=0
b4=32.4
print("a를 논리로 형변환: ", type(a1), bool(b1), type(bool(b1)))
print("b를 논리로 형변환: ", type(a2), bool(b2), type(bool(b2)))
print("c를 논리로 형변환: ", type(a3), bool(b3), type(bool(b3)))
print("c를 논리로 형변환: ", type(a4), bool(b4), type(bool(b4)))

print("*******************")
#문자열로 형변환
c1=3.14
c2=True
c3=200
print("c1를 문자열로 형변환: ", type(c1), str(c1), type(str(c1)))
print("c2를 문자열로 형변환: ", type(c2), str(c2), type(str(c2)))
print("c3를 문자열로 형변환: ", type(c3), str(c3), type(str(c3)))