a=input("Enter 1st side:")
b=input("Enter 2nd side:")
c=input("Enter 3rd side:")
a=int(a)
b=int(b)
c=int(c)
if a+b<c or b+c<a or a+c<b:
    print("no")
else:
    print("yes")