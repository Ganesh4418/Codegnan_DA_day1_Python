integer1=int(input("First integer: "))
integer2=int(input("Second integer: "))
option=int(input("\n1.Add\n2.Subtract\n3.Multiply\n4.Remainder\n5.Quotient\n6.Squares\n7.Cubes\n8.Power\nYour Option: "))
if option==1:
    print(f"Result : {integer1+integer2}")
elif option==2:
    print(f"Result : {integer1-integer2}")
elif option==3:
    print(f"Result : {integer1*integer2}")
elif option==4:
    print(f"Result : {integer1%integer2}")
elif option==5:
    print(f"Result : {integer1//integer2}")
elif option==6:
    print(f"Result : {integer1**integer1},{integer2**integer2}")
elif option==7:
    print(f"Result : {integer1**integer1},{integer2**integer2}")
elif option==8:
    print(f"Result : {integer1**integer2}")
