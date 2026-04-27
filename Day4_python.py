'''
list data types
---- ---- -----
-->list is a collection of different data type
and it is represented by []
separated by commas

any= [1,"python",[2,"fifth",2,53]]
print(any[2][1][4])
any2=[1,"python language",67,68,[36,["this is python class"]]]
print(any2[4][1][0][13])

--> string is immutable
    ------ -- ---------
p="andhra capital hydrabad"
print(p.replace("hydrabad","amaravathi"))

--> list is mutable
    ---- -- -------
list=[1,2,3,4,5,7]
list.append(9)
print(list)

list methods
==== =======
. append()
  -- used to add the element to the list at the last index position
syntax -- var.append()

example
-------
list=[1,2,3,4,5,7]
list.append(9)
print(list)

. extend()
  -- this method is ned to add new element intp list
but Extend adds as each position to each index in the list
extend only takes iterables
syntax -- var.extend()
  
example
-------
a=[123,234,345]
a.extend("python")
print(a)

. pop()
  -- delets the item from the list
pop() removes the value from the list based on given index position
takes exactly one argument
if index is'nt  specified removes the last index postion
syntax--var.pop(index)

example
-------
list=[1,2,3,4,5,7]
list.pop()     #[1, 2, 3, 5]
list.pop(3)    #[1, 2, 3, 5, 7]
list.pop(7)    #IndexError: pop index out of range
print(list)

. remove()
  -- delets the item from the list
remove() removes the value from the list directly
takes exactly one argument
if value is'nt  specified shows type error
syntax--var.pop(index)

example
list=[1,2,3,4,5,7]
list.remove()   #TypeError: list.remove() takes exactly one argument (0 given)
list.remove(3)  #[1, 2, 4, 5, 7]
list.remove(7)
print(list)

Slicing
-------
  -- it is used to get the particular part from the list,string or tuple
  it works based on the index position
syntax-- var[start index:end index]

Example
list=[1,2,3,4,5,6]
print(list[1:5])  #[2, 3, 4, 5]

Len()
-----
  -- used to get the length of the list,string or tuple
syntax -- len(var)

example
list=[1,2,3,4,5,6]
print(len(list))  #6
'''
'''
list data types
mutable & immutable
list methods
append,extend,pop,remove
index,count,insert
slicing.len()
'''


