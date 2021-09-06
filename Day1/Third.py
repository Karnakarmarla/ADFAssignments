#3.	Program to Print all Prime Numbers in an Interval of 5 seconds.
import threading
import time
try:
    def prime(n):
        if (n <= 1):
            print("enter a number greater than 1")
        else:
            for i in range(2,n+1):
                ct=0
                for j in range(2,i+1):
                    if i%j==0:
                        ct=ct+1
                if(ct==1):
                    print(i)
                    time.sleep(5)
    n=int(input("Enter a number"))
    t1=threading.Thread(target=prime(n))
    t1.start()
except:
    print("An error occured")
