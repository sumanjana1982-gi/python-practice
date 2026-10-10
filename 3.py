# Display only those characters which are present at an even index number in given string.
name=input("Enter name:")
for i in range(len(name)):
    if i%2==0:
        print(name[i].upper())


