# 파일 열기

# 파일명/파일목적 순으로 입력
# 한글정보를 위해 utf8 지정
scroe_file = open("score.txt", "w", encoding="utf8")

print("수학 : 0", file=scroe_file)
print("영어 : 50", file=scroe_file)

# 파일을 열면 꼭 닫아야한다.
scroe_file.close()

# 이어쓰기

# w일때는 덮어쓰기가 되기 때문에 이어쓰기인 a로 열기
# write 사용시 기본적으로 줄바꿈이 없다.
scroe_file = open("score.txt", "a", encoding="utf8")
scroe_file.write("과학 : 80")
scroe_file.write("\n코딩 : 100")
scroe_file.close()

# 읽어오기
scroe_file = open("score.txt", "r", encoding="utf8")

# 한번에 다 읽기
print(scroe_file.read())

# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(scroe_file.readline())
print(scroe_file.readline())
print(scroe_file.readline())
print(scroe_file.readline())

# 라인 내용이 있으면 출력 아니면 breack
# 파일이 몇줄인지 모를때 사용
while True:
    line = scroe_file.readline()
    if not line:
        break
    print(line)
scroe_file.close()

# line을 list 형태로 저장
lines = scroe_file.readlines()
for line in lines:
    print(line, end="")
scroe_file.close()