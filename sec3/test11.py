#자료 구조: 기본형(int, float, bool, str), 열거형(list, set, tuple, dict)
#열거형 4가지 괄호 중요
lst = [60,70,50,90,70,80] #list
tp = (60,70,50,90,70,80) #tuple
st = {60,70,50,90,70,80} #set
dct = {'kor':60, 'eng':70, 'mat':50, 'sci':90, 'his':70, 'art':80} #dict(
#dict는 key(항목이름)과 그에 해당하는 값으로 구성된다.
print("리스트:", type(lst),list)  #일반적인 배열구조
print("튜플:", type(tp), tp) #읽기전용 쓰기방지
print("셋:", type(st), st) #순서유지x 중복x->인덱스x
print("딕트:",type(dct), dct)