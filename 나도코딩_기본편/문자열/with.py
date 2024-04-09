import pickle

# 파일을 닫아줄 필요가 없다
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))