from functools import*

lst=[7,3,4,9,10]

result =reduce(lambda x,y: x*y,lst)

print(result)
