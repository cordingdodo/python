#인덱스 및 슬라이싱
name = "kim do yeon is 1004" #변수명 [시작:끝]
print("name[0]: ", name[0]) #인덱스가 0인 데이터
print("name[2:6]=", name[2:6]) #인덱스가 2부터 6전까지의 문자열
print("len(name=", len(name)) #len(변수): 해당 변수의 글자길이
print("name[2:] =", name[2:]) #end값이 생략되면 끝까지
print("name[:6] =", name[:6]) #begin값이 생략되면 처음
print("name[::2] =", name[::2]) #인덱스가 짝수번째인 값
print("name[-2:] =", name[-2:]) #값이 음수이면, 오른쪽부터 