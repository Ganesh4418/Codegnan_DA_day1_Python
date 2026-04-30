'''
user input
==== =====
username=input("enter the username : ")
password=input("password : ")
print("'wifi activated'")


--> user input for int datatype
    ---- ----- --- --- --------

a=int(input())
print(a)

. mapping
  -------
a,b=map(int,input("two numbers : ").split(","))
print(a)
print(type(a))
print(b)
print(type(b))

--> user input for list datatype
    ---- ----- --- ---- --------
lis=list(map(int,input("number sequence : ").split(",")))
print(lis)
print(type(lis))

--> user input for tuple datatype
    ---- ----- --- ----- --------
tup=tuple(map(int,input("number sequence : ").split(",")))
print(tup)
print(type(tup))

--> F string
    - ------
A=int(input())
B=int(input())
print("the sum of two numbers A+B :",A+B)
print(f"the sum of two numbers {A}+{B} : {A+B}")

--> eval()
    ------
a=eval(input())
b=eval(input())
print(a)
print(type(a))
print(b)
print(type(b))

> STATEMENTS
  ----------

--> if else
    -- ----
one=int(input("one number: "))
other=int(input("other number: "))
if one>=other:
    print(f"'Yes It Is {one} is greater than {other}'")
else:
    print(f"'No Its Not {one} is less than {other}'")

--> PROGRAMS
    --------
age=int(input())
if age>=18:
    print(f"your age is {age}, you are good to go")
else:
    print(f"you are {age}, you are under age of {18-age} more years")

marks=int(input())
pass_mark= 35
if marks>=pass_mark:
    print(f"you got {marks} marks, you are pass")
else:
    print(f"you got {marks} marks, you are fail")

'''
