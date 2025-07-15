
#Create a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)


#Create a tuple
tuplex = (4, 6, 2, 8, 3, 1,)
print(tuplex)
#tuples are immutable, so you can not add new new elements
#using merge of tuples with the + operator you can add elemnt and it will create a new tuple
tuplex = tuplex + (9,)


#Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50,)
print(tuple1.count(50))


#Create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#Used tuple[start:start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
#is exclusive
print(_slice)
#If the start index isn't defined, is taken from the beg ining of the tuple
_slice = tuplex[:6]
print(_slice)