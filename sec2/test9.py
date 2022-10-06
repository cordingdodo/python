#반복문 : 해당 조건이나 상황이 만족될 때까지 반복 수행함
i=tot=0
while(i<=10):
    tot+=i #tot=tot+i
    i+=1 #++i , i=i+1
print("0~10 합계: ", tot)

#짝수의 합계
j=aoa=0
while(j<=100):
    aoa+=j
    j+=2
print("0~100까지 짝수의 합계1: ", aoa)

j=aoa=0
while(j<=100):
    if(j%2!=0):
        continue
    aoa+=j
    j+=1
print("0~100까지 짝수의 합계2: ", aoa)

j=aoa=0
while(j<=100):
    if(j%2==0):
    aoa+=j
    j+=1
print("0~100까지 짝수의 합계3: ", aoa)

#무한루프
i=tot=0
while True:
    if(i>100):
        break
    tot+=i
    i+=2
print("0~100까지 짝수의 합계4: ", tot)

i=tot=0
while(i<=100):
    if(i%3==0):
        tot+=i
    i+=1
print("0~100까지 3의 배수의 합계: ", tot)

#홀수의 합계
i=tot=0
while(i<=100):
    tot+=i
    i+=1
print("0~100까지 홀수의 합계1: ", tot)
