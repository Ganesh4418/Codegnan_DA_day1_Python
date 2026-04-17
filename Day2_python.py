'''
NOTES
-----

Operators
---------

Arithmetic Operators
Assignment Operators
Relational Operators
Comparision Operators
Logical Operators
Identity Operators
Membership Operators
BitWise Operators


1. Arithmetic Operators performs arithmetic operations
Like Add(+),Subtract(-),multiply(*),Power(**)
'''
#Execution

num1=90
num2=45
num3=63
print(num1+num2+num3) #O/P --> 198 (Addition operator)

integer1=73
integer2=65
print(integer1-integer2) #O/P --> 8 (subtraction operator)

dig1=144
dig2=2
print(dig1%dig2) #--> 0 (modulus -- returns remainder)
print(dig1%dig2 !=0)# False
print(dig1%dig2 ==0)# True

new_num1=632
new_num2=3
print(new_num1*new_num2) # --> 1896 (multiply)
print(new_num1**new_num2)# --> 252435968 (power)

bill_1=159.37
bill_2=74.3
print(bill_1//bill_2) # --> 2.0 floor division

'''
ASSIGNMENT OPERATORS
---------- ---------

=,+=,-=,*=,**=,//=
'''

#+=
int_=44
int_+=4
int_1=44
int_1=int_1+4
print(int_)
print(int_1)

#-=
minus=23
minus-=3
minus_0=23
minus_0=minus_0-3
print(minus)
print(minus_0)

#*=
mul=450
mul*=6
print(mul)

#**=
po=144
po**=2
print(po)

#//=
div = 52.6
div //= 4.2
print(div)

'''
COMPARISION OPERATOR

==,!=,>,<,<=,>=
'''
M=25
L=9
print (M==L)#Equals to
print (M!=L)#Not Equal to
print (M<L)#Less than
print (M<=L)#Less or Equal
print (M>L)#Greater than
print (M>=L)#Greater or Equal

'''
Logical Operator
AND,OR,NOT

> And - both conditions must be true
> Or - Atleast one conditon must be true
> NOT - reverses the output
'''
ans = 23
ans2 = 31
#AND
print(ans == 5**2 and ans > ans2) # False
print(ans == 5**2 and ans < ans2) # False
print(ans<ans2 and ans == 5**2) # False
print(ans<ans2 and ans>ans2) # True
#OR
print(ans == 5**2 or ans < ans2) # True
print(ans<ans2 or ans == 5**2) # True
print(ans<ans2 or ans>ans2) # True
print(ans>ans2 or ans<ans2) # False
#NOT
print(not(ans>ans2 and ans<ans2)) #True

'''
Identity Operators
-------- ---------
is,is not

> is - used to check object and returns true when the id is same('==' check only the lhs and rhs)
> is not - cused to check object and returns true when the id is not same ('!=' check only the lhs and rhs)
'''
numb=9
sq=3**2
print(numb is sq) #True
print(numb is not sq) #False
print(id(numb)) #140731435681144
print(id(sq)) #140731435681144

'''
Membership Operator
---------- --------
in, not in
'''

list_1 = [5,4,3,6,7]
print(5 in list_1) # True
print(5  not in list_1) # False


'''
Bitwise Operator
------- --------
>& - Bitwise AND
>| - Bitwise OR
>^ - Bitwise XOR

3--> 0101
5--> 0011
0001 --> 1 (Bitwise And for 3&5)
0111 --> 7 (Bitwise Or for 3|5)
0110 --> 6 (Bitwise Xor for 3^5)
'''
print(3&5)
print(3|5)
print(3^5)

