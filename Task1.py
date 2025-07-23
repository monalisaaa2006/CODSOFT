a=float(input("Enter the first number:"))
b=float(input("Enter the 2nd number:"))
operation=input("Enter an operation(+,-,*,/):")

if operation=='+':
    print("Result=",a+b)
    
elif operation=='-':
    print("Result=",a-b)
    
elif operation=='*':
    print("Result=",a*b)
    
elif operation=='/':
    if b!=0:
        print("Result=",a/b)
    else:
        print("Division by zero is invalid")
        
else:
    print("Wrong input")