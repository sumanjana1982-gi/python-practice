def printinfo(arg1,*vartuple):
    print("output is:.......")
    print(arg1)
    for var in vartuple:
        print(var)
    return;
printinfo(10)
printinfo(10,70,20,60)
printinfo(30)
printinfo(40)
