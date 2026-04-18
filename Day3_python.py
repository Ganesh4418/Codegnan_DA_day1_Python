'''
DATA TYPES
---- -----

>Mutable - can be modified directly from the variable where it was initially assigned
- list
- dict

>Immutable - cannot be modified directly from the variable where it was initially assigned
- int
- tuple
- string

types of data types
----- -- ---- -----

-> integer (int) - stores the numbers
. a= 2,b=3

-> float - stores float values (decimal points)
. f=56.3

-> String (str) - stores collection of characters in '',""
. any thing which is written inside ''/"" will be consider as a character
. s="rags",t="riches"

methods
-------
-- syntax --> var_name.method()

--> indexing used to obtain particular substring or an element
from a string,list or tuple by calling with index position
. variable[index number]

--> concatination adds the strings,list,tuple 

> replace() - replaces old string with new string
. var.replace("old str","new str")

> join() - joins the wanted substring after every substring
. " ".join(var)

> split() - used to split the string into individual elements
using a substring and in the from of list
. var.split("substring")

> strip() - used to remove opening index string or closing index string
. var.strip()

> lower()
. var.lower()

> Upper()
var.upper()

an="chiru god of tollywood"
print(an)
_replace = an.replace("chiru","prabhas")
print(_replace)
sp=_replace.replace(" ","_")
print(sp)
print(sp[9])
'''
a="ntr "
b="young tiger"
fact=a+b
print(fact)

gc = ("ramcharan global starzzz")
strip=(gc.strip("z"))
print(strip)

star="rebeL star"
st=star.isupper()
ar=star.islower()
print(st)
print(ar)
pb=star.capitalize()
print(pb)

'''
isdecimal
isalpha
isdigit
isalnum
'''
