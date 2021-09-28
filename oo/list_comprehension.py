lst = []
for i in range(10):
    lst.append(str(i))

#>>> print(lst)
#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

list_comprehension = [str(i) for i in range(10)]

#>>> print(list_comprehension)
#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

"""
Por convenção, se você não usar a variavel, ("i") na list comprehension devemos 
usar no lugar da variavel ("i") o underline "_"
"""