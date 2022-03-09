def smallestnumber(a,b,c):
    if (a<b):
        if (a<c):
            return "A is smallest"

    elif b<c:

            return "B is smallest"
    else:
            return "c is smallest"
x = int(input("Enter the 1st number :"))
y = int(input("Enter the 2nd number :"))
z = int(input("Enter the 3rd number :"))
result = smallestnumber(x,y,z)
print(result)