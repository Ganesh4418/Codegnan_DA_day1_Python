'''
> while statement
- this while statement will keep on executing
until unlesss condition becomes true
ex:
num=1
while num<=5:
    print(num)
    num+=1

> range()
syntax --> range(start,stop,step)
- range function will generate sequence of numbers upto the limit
ex:
limit=int(input("enter limit: "))
for i in range(2,limit+1,2):
    print(i)

nat=int(input("enter limit: "))
for i in range(1,nat+1):
    if i%2==0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")

> break
--> breaks the loop if the iteration satisfies
ex:
actress=["monica belluci","megan fox","jennifer lawrence","ana de armas"]
for i in actress:
    if i =="monica belluci":
        break
    print(i)

> contiue
--> this statement will skip that particular iteration
goes to next iteration
ex:
actress=["monica belluci","megan fox","jennifer lawrence","ana de armas"]
for i in actress:
    if i =="monica belluci":
        continue
    print(i)

> pass
pass is space holder,holds space not to get any error

n=int(input())
count=0
for i in range(2,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime")
else:
    print("not prime")

'''

set_=int(input())
total=0
for i in range (2,set_+1):
    count=0
    for j in range(1,set_+1):
        if i%j==0:
            count+=1
    if count==2:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
