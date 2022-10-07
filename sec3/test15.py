#dict : 키와 값을 동시에 저장하려고 할 경우 활용 = Dictionary
dct1 = {"name" : "kim", "age ": 25, "height":165, "weight":"비밀"}
print(dct1)
print("name 출력: ", dct1["name"]) #특정 원소 읽기 - 변수명["키명"]
dct1["name"]="lee" #특정 원소 값 변경
print("name lee로 변경한 값: " , dct1)

#del dict1["weight"] #원소 제거 /몸무게와 몸무게 값 쌍으로 지워짐
#dct1.clear()   #모든 원소 제거
for key in dct1: #독립시켜서 출력
    print(key, " : ", dct1[key])

#열거형 = 이더레이터 = 컬렉션
#list = 목록[], tuple = 불변(고정) 데이터(), set=모음 또는 집합{}, dict=사전{}
dct2 = {"dodo": 100, "jojo":90, "park":100, "xoxo":70}
print(dct2)
#list -> set, tuple, set -> list, tuple, tuple -> list, set
#list의 tuple 이중 구조
lst0 = [("김도연", 99),("박주언",70),("도도",100),("주주",60)]
print("lst0:", lst0)
dct3=dict(lst0) #안되는듯?
print(dct3)