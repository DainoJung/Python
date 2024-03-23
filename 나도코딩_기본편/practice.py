from random import *

users = range(1, 21)

users = list(users)

shuffle(users)

prize = sample(users, 4)

chicken = prize[0]

coffee = prize[1:]

print(f"-- 당첨자 발표 --\n치킨당청자 : {chicken}\n커피 당첨자 : {coffee}")