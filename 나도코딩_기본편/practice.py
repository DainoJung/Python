from random import *

cnt = 0

for i in range(1, 51):
    time = randrange(5, 50)
   
    if (5 <= time <= 15):
        cnt += 1
        print(f"[O] {i}번째 손님 (소요시간 : {time}분")
    else:
        print(f"[X] {i}번째 손님 (소요시간 : {time}분")

print(f"총 탑승 승객 : {cnt} 분")        
