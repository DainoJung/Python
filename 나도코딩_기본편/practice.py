def std_weight(height, gender):
    if gender == "men":
       return height*height*22
    elif gender == "women":
        return height*height*21

height = 180
gender = "men"

avg_weight = std_weight(height/100, gender)
print(avg_weight)