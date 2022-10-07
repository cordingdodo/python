# 지방, 탄수, 단백질 그램을 키보드로 입력하면 칼로리리를 계산하여 출력하는 프로그램
# 총 칼로리 = 지방*9 + 단백질 *4 +탄수화물 *4
# 총 칼로리(calorie) : 단백질(protein), 지방(jat),
#탄수화물(carbohydrate) 으로 변수선언

jat = int(input("지방 그램수 입력:"))
jatc=jat*9

carbohydrate = int(input("탄수화물 그램수 입력:"))
carbohydratec=carbohydrate*4

protein = int(input("단백질 그램수 입력: "))
proteinc=protein*4

tot=jatc+carbohydratec+proteinc
print("총 칼로리는", tot, "입니다")

