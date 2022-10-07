#함수(function)의 4가지 타입 / 그리고 클래스(class)

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

#호출의 형태
plus1() #매개변수x 리턴x

a = int(input("숫자1: "))
b = int(input("숫자2: "))
plus1(a, b) #매개변수o, 리턴x //매개변수 값 정해줘야함

hap1=plus3() #매개변수x, 리턴o //알아서 프린트됨 //리턴값을 저장하기 위해 hap1등장
print(hap1)

hap2=plus4(a,b) #매개변수o, 리턴o //리턴값 저장하기 위해 hap2등장
print(hap2)

#함수 전달 방법 : 함수의 이름을 호출한다  -> call by name 방식
#매개변수 있는 형식  -> call by value 방식
#함수로 클래스 만든 다음 클래스 객체 전달 -> call by reference 방식
