#Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
for i in range(10):
    for j in range(i-1,i):
        print("current value is ",i,end=" ")
        if j==-1:
                j=0
        print("previous value is",j,end=" ")
        print("sum is",i+j)
    
    
        

