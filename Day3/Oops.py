import sys
import logging
import re
import uuid
from collections import Counter

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler=logging.FileHandler('logFile.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Parent:
   def __init__(self,filename):
        self.filename=filename

   words = []
   with open(sys.argv[1], 'r') as f:
       for line in f:
           for word in line.split():
               words.append(word)

   def prefixcount(self,s):
       try:
            ct = 0
            with open(self.filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        if (word.startswith(s)):
                            ct = ct+1
            logger.info("Number of words have prefix " + s + " are :" + str(ct))
            return ct
       except:
           logger.error("An error occured")
   try:
        def suffixcount(self,s):
            ct = 0
            with open(self.filename, 'r') as f:
                for line in f:
                    for word in line.split():
                        if (word.endswith(s)):
                            ct = ct + 1
            logger.info("Number of words have suffix " + s + " are :" + str(ct))
            return ct

        def maxrepeat(self):
            ct = Counter(self.words)
            logger.info("Maximum repeated word is :" + str((ct.most_common(1))[0][0]))
            return str((ct.most_common(1))[0][0])

        def palindrome(self):
            logger.info("Palindromes are:")
            res=[]
            for word in self.words:
                if (word == word[::-1]):
                    logger.info(word + " ")
                    res.append(word)
            return res

        def toUniqeList(self):
            words = list(set(self.words))
            logger.info(words)
            return words

        def toDict(self):
            words = list(set(self.words))
            dict = {}
            ct = 1
            for x in words:
                dict[ct] = x
                ct = ct + 1
            logger.info("resultant dictionary is :" + str(dict))
            return dict
   except:
        logger.error("An Error Occured")


class Child(Parent):
    def __init__(self,filename):
        self.filename=filename

    try:
        def writeintonewfile(self,filename):
            new_name = str(uuid.uuid4())+".txt"
            words = []
            with open(self.filename, 'r') as f:
                contents=f.read()
                for line in f:
                    for word in line.split():
                        words.append(word)
            spliter = re.split('a|e|i|o|u|A|E|I|O|U', contents)
            newfile = open(new_name, 'w')
            newfile.writelines(spliter)
            newfile.write("\n After Capitalizing 3rd character of every word is :\n")
            for x in words:
                if (len(x) >= 3):
                    w = x[:2] + x[2].upper()
                    if (len(x) > 3):
                        w = w + x[3:]
                    newfile.write(w + " ")
                else:
                    newfile.write(x + " ")
            newfile.write("\n After Capitalizing 5th word is :\n")
            ct = 1
            for x in words:
                if (ct == 5):
                    ct = ct + 1
                    newfile.write(x.upper() + " ")
                else:
                    ct = ct + 1
                    newfile.write(x + " ")
            newfile.write("\n After replacing space with hypen is :\n")
            cont = contents.replace(" ", '-')
            newfile.writelines(cont)
            newfile.write("\n After replacing new line with semicolon is :\n")
            cont = contents.replace("\n", ';')
            newfile.writelines(cont)
    except:
        logger.error("Error occured")



if __name__=="__main__":
    try:
        child1=Child(sys.argv[1])
        logger.info(child1.filename)
        print(child1.prefixcount("to"))
        print(child1.suffixcount("ing"))
        print(child1.maxrepeat())
        print(child1.palindrome())
        print(child1.toUniqeList())
        print(child1.toDict())
        child1.writeintonewfile(sys.argv[1])
    except:
        logger.error("Error occured")
