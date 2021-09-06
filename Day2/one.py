/*1.	Read a text file inputted via argument to the code, perform the below given sequence of actions and write it to new file. 
 a.	Print the number of words having prefix with “To” in the input file.
 b.	Print the number of words ending with “ing” in the input file.
 c.	Print the word that was repeated maximum number of times.
 d.	Print the palindrome present in the file.
 e.	Convert all words into unique list and print in command line
 f.	Create a Word dict with Key as counter index and value as the words present in file and print them on screen.
 g.	Write new file with following actions
     i.	 Split the words based on the vowels
    ii.	 Capitalize 3rd letter of every word 
    iii. Capitalize all characters of every 5th word in the file.
    iv.	 Use – in place of blank space
     v.	 Use ; (semi-colon) for new line.
     vi. Output file name should be generated with unique name.*/
    
    
    
    

import sys,getopt
from collections import Counter
import re
import uuid

def prefixcount(s):
    ct=0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            for word in line.split():
                if(word.startswith(s)):
                    ct=ct+1
    print("Number of words have prefix "+s+" are :"+str(ct))

def suffixcount(s):
    ct = 0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            for word in line.split():
                if (word.endswith(s)):
                    ct = ct + 1
    print("Number of words have suffix " + s + " are :" + str(ct))

def maxrepeat(list):
    ct=Counter(list)
    print("Maximum repeated word is :"+str((ct.most_common(1))[0][0]))

def palindrome(list):
    print("Palindromes are:")
    for word in list:
        if(word==word[::-1]):
            print(word+" ")

def toUniqeList(words):
   words=list(set(words))
   print(words)


def toDict(words):
    words=list(set(words))
    dict={}
    ct=1
    for x in words:
        dict[ct]=x
        ct=ct+1
    print("resultant dictionary is :"+str(dict))


def writeintonewfile(list):
    filename=str(uuid.uuid4())
    f=open(sys.argv[1],'r')
    contents=f.read()
    spliter=re.split('a|e|i|o|u|A|E|I|O|U',contents)
    newfile=open('filename.txt','w')
    newfile.writelines(spliter)
    newfile.write("\n After Capitalizing 3rd character of every word is :\n")
    for x in list:
        if(len(x)>=3):
            w=x[:2]+x[2].upper()
            if(len(x)>3):
                w=w+x[3:]
            newfile.write(w+" ")
        else:
            newfile.write(x+" ")
    newfile.write("\n After Capitalizing 5th word is :\n")
    ct=1
    for x in list:
        if(ct==5):
            ct=ct+1
            newfile.write(x.upper()+" ")
        else:
            ct=ct+1
            newfile.write(x+" ")
    newfile.write("\n After replacing space with hypen is :\n")
    cont=contents.replace(" ",'-')
    newfile.writelines(cont)
    newfile.write("\n After replacing new line with semicolon is :\n")
    cont = contents.replace("\n", ';')
    newfile.writelines(cont)


words = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        for word in line.split():
            words.append(word)

prefixcount("To")
suffixcount("ing")
maxrepeat(words)
palindrome(words)
toUniqeList(words)
toDict(words)
writeintonewfile(words)
