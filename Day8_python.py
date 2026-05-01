'''
> elif
  ----
  else if method gives more options to get the result

EXAMPLE :
-------
marks=int(input())
if marks>=90:
    print("A+")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
elif marks>=35:
    print("E")
else:
    print("FAIL")

    
> Nested if
  ------ --
  if statement inside another if statement
  
EXAMPLE
-------
bank_info={"atm pin":"0904"}
atm_pin=input("enter pin : ")
if len(atm_pin)==4:
    if atm_pin in bank_info['atm pin']:
        print("you're good to go")
    else:
        print("incorrect pin")
else:
    print("enter 4 digit pin")


> for loop
  --- ----
 for statement is used to iterate over items
 like (string,int,tuple,list) with fixted no. of iterations

EXAMPLE
-------
loop_list=[23,45,6,78]
for i in loop_list:
    print(i)
else:
    print("loop closed")

> else in for loop
  ---- -- --- ----
  after completing the iterations else will be executed

PALINDROME
----------

word = input()
dup=""
for i in word:
    dup=i+dup
if dup == word:
    print("yes palindrome")
else:
    print("No palindrome")
'''
