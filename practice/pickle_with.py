
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "남희정", "나이" : 28, "취미" : ["영화 감상", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 잇는 정보를 파일에 저장.
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# close를 쓸 필요 없음

with open("study.txt", 'w', encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있습니다.")

with open("study.txt", "r", encoding='utf8') as study_file:
    print(study_file.read())

