#2.	Program to read a CSV (CSV with n number of columns) and store it in DICT of list. 
try:
    import csv
    ex=[]
    with open("E:\ADF Assignments/secondInput.txt",mode='r') as file:
        for val in csv.DictReader(file):
            ex.append(val)
    print(ex)
except:
    print("An error occured")
