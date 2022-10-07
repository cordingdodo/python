#임의의 1~45 의 여섯 개 숫자를 출력하도록 하되, 중복이 허용되지 않는 로또 번호 발생 프로그램을 작성해라
import random
lst1=[0,0,0,0,0,0]
for i in range(6):
    lst1[i]=random.randint(1,45)
    print(lst1[i])
