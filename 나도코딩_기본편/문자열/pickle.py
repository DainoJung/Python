# pickle이란?
# 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장하는것

import pickle

# # 쓰기
# b -> 바이너리타입을 항상 같이 지정해줘야함
# 따로 인코딩 지정해줄 필요 X
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이":30, "취미": ["축구", "골프", "코딩"]}

# profile에 있는 정보를 file에 저장
pickle.dump(profile, profile_file)
profile_file.close()

# 읽기
profile_file = open("profile.pickle", "rb")
# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()