#7.	Program to get an application (name , age , gender, salary, state, city).
try:
    x = list(map(str, input("Enter name , age , gender, salary, state, city values: ").split()))
    print("name:"+x[0])
    print("age:"+str(x[1]))
    print("gender:"+x[2])
    print("salary:"+str(x[3]))
    print("state:"+x[4])
    print("city:"+x[5])
except:
    print("An error occured")
