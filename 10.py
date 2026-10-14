
number=[]
sum=0
count=0
print("type 'ex' to stop listing ....")
while True:
 num=int(input(f"{count}.Enter product price of  :"))
 number.append((num))
 sum+=(num)
 count+=1
 if num==10000:
             break

    
print(f"list of product price :{number[:count-1]}")
sum=sum-10000
if sum>=800:
    sum=sum-(sum*10)/100
print(f"Total amount of product is :{sum}")
#print("vvv",count)
