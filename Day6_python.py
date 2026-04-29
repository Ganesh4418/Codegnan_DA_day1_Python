'''
Set Data type
--- ---- ----
> set is a collection of unordered elements or unique
unlike list or tuple  set is not permit the duplicates in it
> set is mutable
ex:set={1,2,3,5,6,3}

set methods
--- -------
> add()
- syntax--var.add(element)

set={1,2,3,5,6,3}
set.add(9)
print(set) #{1, 2, 3, 5, 6, 9}

> remove()
- syntax--var.remove(element)

set={1,2,3,5,6,3}
set.remove(3)
print(set) #{1, 2, 5, 6}

> pop()
- syntax--var.pop(no args)

set={1,2,3,5,6,3}
set.pop()
print(set) #{2, 3, 5, 6}

> clear()
- syntax--var.clear()

set={1,2,3,5,6,3}
set.clear()
print(set) #set()

> update()
- syntax--var.update([elements])

set={1,2,3,5,6,3}
set.update([9,12,34,15])
print(set) #{1, 2, 3, 5, 6, 9, 12, 15, 34}

> union()
- syntax--var.union([elements])
- set_1|set_2

set={1,2,3,5,6,3}
setu={9,12,2,3,5,34,15}
u=set.union(setu)
print(u) #{1, 2, 3, 34, 5, 6, 9, 12, 15}
print(set|setu)#{1, 2, 3, 34, 5, 6, 9, 12, 15}

> intersection()
- syntax--var.intersection([elements])
-set_1&set_2ou

set={1,2,3,5,6,3}
setu={9,12,2,3,5,34,15}
i=set.intersection(setu)
print(i)#{2, 3, 5}
print(set&setu)#{2, 3, 5}


> difference()
- syntax--var.difference([elements])
- set_1-set_2/set_2-set_1

set={1,2,3,5,6,3}
setu={9,12,2,3,5,34,15}
i=set.difference(setu)
i2=setu.difference(set)
print(i)#{1, 6}
print(i2) #{9, 34, 12, 15}
print(set-setu)#{1, 6}
print(setu-set) #{9, 34, 12, 15}


type convertions
---- -----------
 int to string,float
-->
a=8
print(type(a))#<class 'int'>
b=str(a)
c=float(a)
print(type(b)) #<class 'str'>
print(type(c)) #<class 'float'>
print(b) #8
print(c) #8.0

 float to string,int
-->
a=8.7
print(type(a))#<class 'float'>
b=str(a)
c=int(a)
print(type(b)) #<class 'str'>
print(type(c)) #<class 'int'>
print(b) #8.7
print(c) #8

 string to int,float,list,tuple
only possible with string containing numbers
-->
a="99"
print(type(a))#<class 'str'>
b=int(a)
c=float(a)
x=list(a)
y=tuple(a)
print(type(b)) #<class 'int'>
print(type(c)) #<class 'float'>
print(type(x)) #<class 'list'>
print(type(y)) #<class 'tuple'>
print(b) #99
print(c) #99.0

Set Data type
set methods
-add
-remove
-pop
-clear
-update
set operations
-union
-intersection
-difference
type convertions
int to string,float
float to string,int
string to int,float,list,tuple
list to tuple
'''
