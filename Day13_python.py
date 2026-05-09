'''
def sum(a,b):
    return a+b
result=sum(2,8)
print(result)

--> print statement shows out put on the screen
--> return statement sends a value back
to the caller function to reuse

inbuilt functions

len()
max()
min()
range()

lis=[4,5,6,5,7,33]
print(len(lis))
print(max(lis))
print(min(lis))

start=int(input())
end=int(input())
for i in range(1,end+1):
    print(f"{start}x{i}={start*i}")
'''
def tables(start,end):
    for i in range(1,end+1):
        print(f"{start}x{i}={start*i}")
tables(start=int(input()),end=int(input()))

