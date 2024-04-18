class BigNumError(Exception):
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    num1 = int(input())
    num2 = int(input())
    if num1 >= 10 or num2 >= 10:
        # 에러 발생
        raise BigNumError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, num1/num2))
except ValueError:
    print("잘못된 값 입력. 한자릿수만 가능")
except BigNumError as err:
    print("에러가 발생")
    print(err)
finally:
    print("계산기 종료")