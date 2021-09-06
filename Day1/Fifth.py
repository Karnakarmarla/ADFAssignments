try:
    def binary(n):
        sum=""
        while n>=2:
            sum=str(n%2)+sum
            n=n//2
        sum=str(n)+sum
        print("Decimal to Binary is "+sum)
    def octal(n):
        sum=""
        while n>=8:
            sum=str(n%8)+sum
            n=n//8
        sum=str(n)+sum
        print("Decimal to Octal :"+sum)
    def hex(n):
        sum=""
        l=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        while n>=16:
            sum=l[n%16]+sum
            n=n//16
        sum=l[n]+sum
        print("Decimal to Hexadecimal:"+sum)
    n=int(input("Enter a Decimal number"))
    binary(n)
    octal(n)
    hex(n)
except:
    print("An error occured")

    