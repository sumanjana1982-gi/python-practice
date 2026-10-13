#
n=int(input("Enter a number: "))
result=1
for i in range(n,1,-1):
    
    result=result*i
   # print(result)

print(f'factorial of {n} is {result}')
