# 튜플(tuple) : 읽기 전용 - immutable(고정) 자료형으로 한 번 데이터가 저장되면 변화되지 않음 (지우거나 변경x)
tp=(124, False, "lee")
print(tp[0])
#tp[1]=True   #tp[1]=True 변경 불가능 / 튜플은 원소 변경 불가능
print(tp)
lst=list(tp)
print(lst)
lst[1]=True
tp=tuple(lst)
print(tp)
a=tp[0:2]
print("a : ", a)
b=tp[:3]
print("b : ", b)
c=tp[1:]
print("c : ", c)
d=tp[::2] #짝수번째 것만
print("d : ", d)
e=tp[::-1] #값이 거꾸로
print("e : ", e)

dt1=[10,20,30,40] #리스트
dt2=(10,20,30,40) #튜플
dt3=(50,60,70,80)
dt4=dt2+dt3
print("dt2: ", dt2)
print("dt3: ", dt3)
print("dt4: ", dt4) #튜플 합치기 가능
lst = dt1 * 3 #반복 / 3번 반복 
print("dt1*3 : ", lst)
lst2= [num*3 for num in dt1] #내포 : 원래 원소 데이터에 *3 하여 할당/ 원소 값에 곱하기3
print("num 함수로 lst2 : ", lst2)

#튜플도 되는지 보자!
tp1=dt2 * 3 #원소값 건들이지 않아서 가능 / #반복
print("dt2 * 3: ", tp1)
tp2=[num*3 for num in dt2] #튜플의 내포는 원칙적으로 불가능해서 리스트의 내포를 활용함
tp2=tuple(tp2) #그러고 다시 튜플로 형변환
print("num 함수로 tp2*3 : ", tp2)

first, second, third, fourth = tp2 #할당 /분리됨 / 갯수 알 때
data1, *data2 = tp2 #할당 맞지 않을땐 첫번째 데이터는 data1에 들어가고 나머지 data2에 들어가고 모두 리스트로 바뀜 / 갯수 모를 때 
print(first, second, third, fourth)
print(data1, data2)