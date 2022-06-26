# #  takes in two lists as parameters and returns the first list concatenated to the second list
# a = [5,2,4,5]
# b = [7,8,6,5]
# def concat(a,b):
#     a = (b+a)
#     return a
# print(concat(a,b))

# #  takes in a list and reverses it
# a = [1,2,3,6,23,2,1]
# def reverse(a):
#     b = []
#     for i in range(len(a)):
#         b = [a[i]] + b
#     return b

# print(reverse(a))


# Takes in a list of lists of integers and returns the sum
my_list = [[2,4,6],[4,7,6],[1,3]]
def list_sum(my_list):
    a = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            a = a + (my_list[i][j])
    return a

# print(list_sum([[1,2],[3,4]])) # returns  10
# print(list_sum([[],[3,4]])) # returns 7
# print(list_sum([[1,2,3,4],[1,2],[1,2]])) # returns 16

print(list_sum(my_list))