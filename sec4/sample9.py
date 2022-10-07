#급여 처리 프로그램 작성하기
#키보드로 총 근무시간, 기본급 등을 입력받아 총 급여를 계산해 출력하기
#총 급여=기본급+상여금+시간외수당
#상여금은 기본급 25%
#시간 외 수당은 정규 근무시간이 160시간이므로 그 시간을 초과하는 시간을 초과근무시간
#시간외수당은 초과근무시간 당 기본급의 200을 나눈 값의 초과근무시간을 곱한 값

hour=int(input("총 근무 시간"))
nor=int(input("기본급"))
bonus=float(nor/4)
if(hour>=160):
    overtime=hour-160 #초과근무시간
else:
    overtime=0
overtimepay=float(overtime*(nor/200))
tot=nor+bonus+overtimepay
print("총 급여는", tot, "원입니다.")
#tot=nor+상여금+시간외수당