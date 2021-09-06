#1.	Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.
import re

try:
    words=[]
    with open('FirstInput.txt', 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)


    words=list(set(words))
    words=list(sorted(words, key = len))
    with open('FirstOutput.txt', 'w') as f:
        for i in words:
            f.write(i+str(",")+str(len(i)))
            f.write("\n")
except:
    print("An exception occurred")
