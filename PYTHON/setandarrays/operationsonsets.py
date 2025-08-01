
# Different types of sets in Python
# Set of integers
my_set = {1, 2, 3}


#Set of mixed datatypes
my_set = {1.0, "Hello", (1,2,3)}
print(my_set)

# Set cannot have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)


#We can make set from a list
my_set = set([1,2,3,2])
print(my_set,["\n"])


#Remove a number from set
num_set = set([0,11,2,3,4,5])
print("Oringinal set:")
print(num_set)
num_set.pop()
print("After removing the first element from the said set:")
print(num_set, "\n")