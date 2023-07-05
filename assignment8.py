# Write a Python program to square the elements of a list using map() function.


# Sample List:  [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]


# solution
#Sample_list
number = [4,5,2,9]
def square(x):
    return x**2
square_number = list(map(square, number))
print("Square the elements of the list")
print(list(square_number))