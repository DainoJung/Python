url = "http://naver.com"

my_str = url.replace("http://", "")

my_str = my_str[:my_str.index(".")]

password = f"{my_str[:3]}{len(my_str)}{my_str.count('e')}!"

print(password)