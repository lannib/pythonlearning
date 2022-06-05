def my_function():
    print("this is my function")
    print("functions are very cool")

# my_function()
# my_function()

def my_function_with_arguments(parameter_one, parameter_two):
    print(parameter_one)
    print(parameter_two)

# my_function_with_arguments("hello", "there")

# Write a function called average that takes in two integers that takes in two integers and prints their average

def average(parameter_one, parameter_two):
    print(int((parameter_one + parameter_two) / 2))

# average(5, 15)



# returns
def add_two(my_num):
    # print(my_num+2) would not recommend
    return my_num+2


# result = add_two(5)
# print(result)
# print(add_two(5)) #both of these return the result of the function, either works


def can_i_sleep_in(weekend, morning_plans):
    # return True and (not False)

    return weekend and (not morning_plans)

# print(can_i_sleep_in(True, False)) # can be explicit and say weekend = True, morning_plans = False, can also swap order of arguments if you are explicitly defining values

# print(not True) # false
# print(True and False) # False
# print(True and True) # True
# print(False and False) # false
# print(False and True) # False


# print(True or False) # True
# print(True or True) # True
# print(False or False) # False
# print(False or True) # True









def can_i_go_to_the_beach(sunny, temp_over_80, windy):
    return sunny and temp_over_80 and not windy

# print(can_i_go_to_the_beach(True, True, False))
# print(can_i_go_to_the_beach(False, True, False))
# print(can_i_go_to_the_beach(False, False, False))
# print(can_i_go_to_the_beach(True, True, True))



# print("hello"==43567) # checks if two things are equal to each other
# print("hello"=="hello")
# print(43567==43567)
# print(10>11)
# print(10<11)
# print(10>=11)
# print(10<=11)

# print(43567!=43567) # checks if two things are unequal to each other


def should_i_go_outside(temp):
    # return true if temp is greater than or equal to 80
    return temp>=80 #(this would be the preferred way to write this)

    # if (temp>=80 and temp<=105):
    #     return True
    # else:
    #     return False

# print(should_i_go_outside(80))







def has_teen(a, b, c):
    # return true if one of these numbers is a teen
    # if any of them are not, return false
    return (a >= 13 and a <= 19) or (b >= 13 and b <= 19) or (c >= 13 and c <= 19)


print(has_teen(10, 10, 5))
print(has_teen(10,13,19)==True)
print(has_teen(16,13,19)==True)
print(has_teen(10,13,10)==True)
print(has_teen(10,13,19)==True)
print(has_teen(16,13,19)==True)
print(has_teen(9,10,20)==False)











# write a function named round_fun that takes in a float and rounds it
# round_fun(10) should return 10.0

# def round_fun(my_float)
