print("Python", "Java", sep=" vs ")

# 출력값 : Python vs Java

print("Python", "Java", end="?")
print("무엇이 승자인가")

# 출력값 : Python Java?무엇이 승자인가
# 기본값이 줄바꿈으로 설정되어있다.


# 정렬

scores = {"수학": 0, "영어" : 50, "코딩" : 100}

# ljust(8) 8칸 차지하고 좌측 정렬
# rjust(4) 4칸 차지하고 우측 정렬
for subject, scroe in scores.items():
    print(subject.ljust(8), str(scroe).rjust(4), sep=":")

""" 출력값
수학      :   0
영어      :  50
코딩      : 100
"""

# 빈공간 0 채우기

# 3개의 공간에서 빈 공간을 0으로 채운다.
for num in range(1, 6):
    print("대기번호 : " + str(num).zfill(3))
    
"""
대기번호 : 001
대기번호 : 002
대기번호 : 003
대기번호 : 004
대기번호 : 005
"""

# 표준입력

answer = input("아무 값이나 입력하세요 : ")

print(type(answer))
# 항상 문자열로 저장
# 출력값 : str

print("입력하신 값은 " + answer + "입니다.")