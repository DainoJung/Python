gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f"[함수 내_전여변수] 남은 총 : {gun}")
    
    
def checkpoint2(soldiers):
    gun = 20 # 지역변수 : 함수 내에서만 사용 가능
    gun = gun - soldiers
    print(f"[함수 내_지역변수] 남은 총 : {gun}")
    
print(f"전체 총 : {gun}")
checkpoint(2)
checkpoint2(2)
print(f"남은 총 : {gun}")
