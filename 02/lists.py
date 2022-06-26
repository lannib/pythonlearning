# list
# a = [1, 2, 3, 4, 5]

# print(a)

# lists can contain anything
# # STRINGS
# a = ["hello", "there"]
# # booleans
# a = [True, True]
# # A mix of datatypes
# a = [True, "Jackson", [1, 2, 3]]

# list functions

# length of a list
# print(len(a))


my_list = ['a', 'b', 'c', 'd']

# print(my_list[0]) #this gets me a
# print(my_list[3]) #this gets me d


# iterating over lists
# # i is the index
# for i in range(len(my_list)):
#     print(my_list[i])

# # for each loop
# for my_item in my_list:
#     print(my_item)    



# These are non mutable ways to change a list
# empty list
# a = []
# # add an item to the list
# a = a + [1]
# print(a)
# # concatenate two lists
# print([1,2,3]+[4,5,6])





# # Mutable methods
# # # empty list
# a = []
# # # add an item to the list
# a.append('dickbutt')
# print(a)
# # # concatenate two lists
# # print([1,2,3]+[4,5,6])


# scope of mutable methods

# def my_function(var1, var2):
#     return var1 + var2

# # not recommended
# def my_function(var1, var2):
#      var1.extend(var2)
#      return var1
 
# a = [1,2,3]
# b = [4,5,6] 
# print(a)
# print(b)
# print(my_function(a,b))
# print(a)
# print(b)




# # upper() is non-mutable so must declare new a value or print line separately for the result
# a = 'abc'
# a = a.upper()
# print(a)

# strings, ints, bools, and floats are not mutable "primitive data types"
# lists and any other classes/objects can have mutable methods

# Given an array of ints, return the number of 9's in the array.


# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

nums = [9,5,9,1,2]

a = 0

# def array_count9(nums):
#   a = 0
#   for i in range(len(nums)):
#     if nums[i] == 9:
#       a = a + 1
#   return a

# print(array_count9(nums))


def array_front9(nums):
  for i in range(len(nums)):
    if range(len(nums[i])) <= 4 and nums[i] == 9:
      return True
  return

print(array_front9(nums))



# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


# def array_front9(nums):
#   for i in range(len(nums)):
#     if i <= 3 and nums[i] == 9:
#       return True
#   return False

print(array_front9(nums))