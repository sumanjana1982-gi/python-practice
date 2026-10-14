n=int(input("Enter number of elements:"))
number=[]
for i in range(n):
    num=int(input("Enter elements:"))
    number.append(num)
print(f'list of elements  you entered are {number}')
max=number[0]
for i in range(1,n):
    if number[i]>max:
        max=number[i]
print(f'maximum number in the list is {max}')
min=number[0]
for i in range(1,n):
    if number[i]<min:
        min=number[i]
print(f'minimum number in the list is {min}')