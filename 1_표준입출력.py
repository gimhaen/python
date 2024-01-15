# %% 블럭 만들기는  shift + Enter
# 표준 출력 print()
num = 20
name = '홍길동'
print("내소개 :", name, ",",num)

# 여러줄을 동시에 입력
test = '''
Life is too short
You need python
'''
print(test)
# %%
# 문자열에 변수를 넣는 3가지 방법
# (1) %-포맷팅 %s 문자형 %d 정수형 %f 실수형 / 변수명이 넘 길면 이거 쓰는거 추천
text = "My name is %s, My age is %d" % ("홍길동", 30)
print(text)

text = "My name is %s, My age is %d" % (name, num)
print(text)

# (2) {}-포맷팅
text = "My name is {}, My age is {}".format("홍길동", 30)
print(text)

text = "My name is {}, My age is {}".format (name, num)
print(text)

# (3) f-포맷팅 <파이썬 3.6버전부터 지원>
text = f"My name is {'홍길동'}, My age is {30}"
print(text)

text = f"My name is {name}, My age is {num}"
print(text)

#{}안에 표현식<함수, 연산자, 변수 등의 처리결과>을 넣을 수 있음
text = f"My name is {name+'님'}, My age is {num+5}"
print(text)
# %%
# 자릿수 및 정렬
# (1) %-포맷팅 %s 문자형 %d 정수형 %f 실수형 / 변수명이 넘 길면 이거 쓰는거 추천
text = "My name is %20s, My age is %4d" % ("홍길동", 30) #오른쪽 정렬 
print(text)

text = "My name is %-20s, My age is %5.1f" % (name, 31.45) #왼쪽 정렬(-) , f 최대 다섯자리까지 소수점은 한자리까지만
print(text)

# (2) {}-포맷팅
# > : 오른쪽, < : 왼쪽, ^ : 가운데 정렬
text = "My name is {:>20}, My age is {:<20}".format("홍길동", 30)
print(text)

text = "My name is {:^10}, My age is {:^10}".format (name, num)
print(text)

floatNum = 31.4585
text = "My name is {:^10}, My age is {:^10.3f}".format (name, floatNum)
print(text)

# (3) f-포맷팅 <파이썬 3.6버전부터 지원>
text = f"My name is {'홍길동':>20}, My age is {30:<20}"
print(text)

text = f"My name is {name:->20}, My age is {num:a^20}"
print(text)

# %%
# print() 끝문자 변경
print("사과")
print("포도")

# 자동 개행을 없애고 싶을 때
print("사과", end='')
print("포도")

print("사과", end='-----------')
print("포도")
# %%
# 문자열 덧셈과 곱셈

#1) 문자열 덧셈 : 문자열끼리 붙여줌
str1 = "사과"
str2 = "포도"
str3 = str1 + " " + str2
print(str3)

#2) 문자열 곱셈 : 문자열을 반복함
print(str1*3)

# %%
# 표준 입력
print("문자열을 입력하세요>", end='')
inStr = input() #키보드로부터 입력받아 문자열로 변환 ctrl + Enter 하면은 입력 창 뜸
print(inStr)

# %%
inStr = input("문자열을 입력하세요>")
print(inStr)
# %%
numStr = input("정수를 입력하세요 >")
# print(numStr + 4) # 타입에러!
print(int(numStr) + 4) #문자열로 숫자 받아져서 int로 숫자 변환 해줘야 오류 안남

# %%
numStr = float(input("실수를 입력하세요 >")) # input을 아예 감싸버려
print(numStr * 3.14)

# %%
# Quiz
# 섭씨 온도를 입력받아서 화씨 온도로 변환하는 프로그램 작성
# 화씨 온도 = 섭씨 온도 * 1.8 + 32
# 화씨 온도를 출력할 때 소수점 2째 자리까지만 표시

C = float(input("섭씨 온도를 입력하세요 >"))
F = C * 1.8 + 32
print(f"화씨 온도는 {F:.2f}도 입니다")
# %%
2