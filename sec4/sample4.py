#컴퓨터에서 1~10의 임의의 수를 발생시키고 사용자가 입력한 수가 일치하면, 미션성공으로 출력하고
#만약, 일치하지 않으면 불일치로 출력하며, 일치할 때까지 사용자의 숫자 입력은 계속된다.

import random
lst1 = [0, 0, 0, 0, 0]
for i in range(5):
    lst1[i] = random.randint(1, 10)
    print(lst1[i])

while True:
    lst2 = []
    a = int(input("1~10까지 수 5개를 하나씩 입력하세요:"))
    lst2.append(a)
    b = int(input("1~10까지 수 5개를 하나씩 입력하세요:"))
    lst2.append(b)
    c = int(input("1~10까지 수 5개를 하나씩 입력하세요:"))
    lst2.append(c)
    d = int(input("1~10까지 수 5개를 하나씩 입력하세요:"))
    lst2.append(d)
    e = int(input("1~10까지 수 5개를 하나씩 입력하세요:"))
    lst2.append(e)
    print(lst2)
    if(lst1==lst2):
        print("미션 성공")
        break
    else:
        print("불일치")