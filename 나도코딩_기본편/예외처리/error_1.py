try:
    print("나누기 전용 계산기")
    nums = []
    nums.append(int(input("첫 번째 숫자 : ")))
    nums.append(int(input("두 번째 숫자 : ")))
    nums.append(nums[0] / nums[1])
    
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

except ValueError:
    print("에러! 잘못된 값 입력")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러 발생")
    print(err)