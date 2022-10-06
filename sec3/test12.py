# 리스트: 요소를 선언, 추가, 삽입, 수정, 삭제, 정렬
# 인덱스가 존재하여 순서 제어가 가능함
a=[] #빈리스트
b=["kim", 1004, 6.28, True]     #python은 각기 다른 데이터 타입을 저장 가능함
print(id(b), type(b), b)
print(id(b[0]), type(b[0]), b[0])    #변수명[인덱스] : 특정 번째 데이터
print(b[1:3])    #b 1부터 3전까지 #인덱스가 1인 요소부터 2인 요소까지
print(b[0:])     #0번째부터 끝가지
print(b[1:])     #1번째부터 끝까지
print(b[0:4:2])  #0번째부터 짝수만?
print(b[::2])
print(b[::-1])
b.append(18)    #b[4]=18 #b 18요소 추가됨
print(b)
del b[1]     #b 1번 요소 삭제되고 뒤에꺼 땡겨옴 #b[1]가 제거되면서 뒤에 요소 당겨옴
print(b)
b[3]=1004   #b[3]의 저장값을 1004로 변경
print(b)
b.insert(2, "Angel")     #b[2] 원소를 삽입 #원래 b[2]는 뒤로 밀려남
print(b)

c=["park", 100, "A", False]
d=b+c   #요소 합치기
print(d)
comment = "My name is doyeon, kim park, lee, kim, han, park, kang"
e=comment.split(sep=' ') #''마다 쪼개줌  #리스트로 만들어줌  #요소 분리
print(e)
print("kim의 인덱스: ",e.index('kim')) #특정 원소 위치(인덱스) 찾기 #but 여러개/요소가 없을땐 에러남
print("개수: ", e.count('park,')) #특정 원소의 개수 구하기
print("전체 원소의 수: ", len(e))

e= [90, 40, 100, 70, 60, 80, 50]
print("정렬 전: ", e)
f=e.sort()      #오름차순 정렬
print("오름차순 정렬: ", e)
g=e.reverse()   #내림차순 정렬
print("내림차순 정렬: ", e)
# e.remove(2) #인덱스 2인 원소 제거
print("")
e.pop() #스택(LIF0) 연산 /선입후출 = 가장 마지막 데이터 끌어냄
print("pop() 연산 후", )
e.pop(1) #인덱스 1 제거 #특정 인덱스 위치의 원소 끌어냄(제거)
print("pop(1) 연산 후", e)
e.extend([90,80])
print("확장 후: ",e)
help(list)