#함수(function) 그리고 클래스(class)
#매개변수 없고, 리턴값도 없음
def plus1():
    print("더하기")

#매개변수 있고, 리턴은 없음
def plus2(a, b):
    print(a+b)

#매개변수 없고, 리턴 있음
def plus3():
    a=int(input("숫자1: "))
    b=int(input("숫자2: "))
    return a+b

#매개변수 있고, 리턴 있음
def plus4(a,b):
    return a+b