#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
product=a*b
if product<1000:
    print("product is:",product)
else:
    print("Sum is :",a+b);
