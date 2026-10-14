from datetime import datetime

print(datetime.now())
number=[]
sum=0
count=0
print("type '10000' to stop listing ....")
while True:
    num=int(input(f"{count}.Enter product price of  :"))
    number.append((num))
    sum+=(num)
    count+=1
    if num==10000:
        break



Subtotal=sum-10000
Discount=(Subtotal*10)/100
total=Subtotal-Discount
if sum>=800:
    sum=sum-(sum*10)/100
print("\n" + "=" * 32)
print("          SMART MART")
print("         CASH RECEIPT")
print("=" * 32)

print("Bill No:", datetime.now().strftime("%Y%m%d%H%M%S"))
print("Date:", datetime.now().strftime("%d-%m-%Y %I:%M %p"))

print("-" * 32)
print(f"{'ITEM':<18}{'PRICE':>14}")
print("-" * 32)

for i, price in enumerate(number[:count-1], start=1):
      print(f"{('Product ' + str(i)):<18}₹{price:>12.2f}")
      print("-" * 32)
print(f"{'Subtotal':<18}₹{Subtotal:>12.2f}")
print(f"{'Discount':<18}₹{Discount:>12.2f}")
print("-" * 32)
print(f"{'TOTAL PAID':<18}₹{total:>12.2f}")
print("=" * 32)
print("      THANK YOU! VISIT AGAIN")
print("=" * 32)

      


