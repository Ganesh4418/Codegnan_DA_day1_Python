'''
list=[23,5,6,1,4]
list.sort()
print(list)
print(sorted(list))
list.append(8)
print(list)

-> Tuple
- it is a collection of elements of different datatypes
- that are represented by paranthesis ()
- the items in the tuple is separated by commas
- tuple is immutable

Example:
tup = ("code",1,2,4.5,(0,1,2),[7,3])
print(tup[5][1])

tuple=(1,"2",4,3)
tuple2=(6,7,9)
print(tuple+tuple2)

-> Dictionary (dict)
   ----------  ----
-- dict is a collection of imutable keys(string,int,tuple)
and mutable and immutable value pairs
-- represented between {}
-- key dont allow the duplicates
-- value may have duplicates
Example:
dic={"100":"crores",
     73:67,
     "lord":"labakku"
     }
print(dic)
print(dic.keys())

Methods
-------
> keys()
  ------
-- used to access only keys in the dict
syntax - dict.keys()
-- Example:
dic={"100":"crores",
     73:67,
     "lord":"labakku"
     }
print(dic.keys())

> values()
  --------
-- used to access only values in the dict
syntax - dict.values()
-- Example:
dic={"100":"crores",
     73:67,
     "lord":"labakku"
     }
print(dic.values())

> items()
  -------
-- used to access only key-value pair in the dict
syntax - dict.items()
-- Example:
dic={"100":"crores",
     73:67,
     "lord":"labakku"
     }
print(dic.items())

> clear()
  -------
-- used to empty the entire dictionary
syntax - dict.clear()
-- Example:
dic={"100":"crores",
     73:67,
     "lord":"labakku"
     }
dic.clear()
print(dic)

> Update()
  --------
-- used to  update new key value pair to the dict
syntax - dict.update({key:value})
-- Example:
dic={"100":"crores",
     73:67,
     "lord":"labakku"
     }
dic.update({"key":"value"})
print(dic)
'''
'''
sort()
sorted()
Tuples
Dictionary
Methods
-keys()
-values()
-items()
-clear()
-Update()
'''
