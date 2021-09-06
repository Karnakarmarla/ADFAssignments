#4.	Program to Find HCF or GCD.
try:
    n=int(input("Enter number1"))
    m=int(input("Enter number2"))
    while(m!=0):
        t=m
        m=n%m
        n=t
    print(n)
except:
    print("An error occured")
