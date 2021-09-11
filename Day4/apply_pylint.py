""" After Applying changes as per Pylint and got 9.71/10 """
import sys
import logging
import re
import uuid
from collections import Counter


class Parent:
    """Example for parent class"""
    def __init__(self,filename):
        self.filename=filename

    words = []
    with open(sys.argv[1], 'r',encoding='utf8') as file:
        for line in file:
            for word in line.split():
                words.append(word)

    def prefix_count(self,prefix_str):
        """Used for prefix count of a word"""
        try:
            count = 0
            with open(self.filename, 'r',encoding='utf8') as file:
                for line in file:
                    for word in line.split():
                        if word.startswith(prefix_str):
                            count = count+1
            logger.info("Number of words have prefix %s are :%s",prefix_str, str(count))
            return count
        except Exception:
            logger.error("An error occured")
    try:
        def suffix_count(self,suffix_str):
            """Used for suffix count"""
            count = 0
            with open(self.filename, 'r',encoding='utf8') as file:
                for line in file:
                    for word in line.split():
                        if word.endswith(suffix_str):
                            count = count + 1
            logger.info("Number of words have suffix %s are :%s",suffix_str,str(count))
            return count

        def max_repeat_word(self):
            """Used for finding maximum repeated word"""
            count = Counter(self.words)
            logger.info("Maximum repeated word is :%s" , str((count.most_common(1))[0][0]))
            return str((count.most_common(1))[0][0])

        def palindrome(self):
            """Prints all the palindromes present in file"""
            logger.info("Palindromes are:")
            res=[]
            for word in self.words:
                if word == word[::-1]:
                    logger.info("%s  ",word)
                    res.append(word)
            return res

        def to_unique_list(self):
            """Prints unique list of words"""
            words = list(set(self.words))
            logger.info(words)
            return words

        def to_dict(self):
            """prints dict of index, word as Key-Value pairs"""
            words = list(set(self.words))
            dict_of_words = {}
            count = 1
            for word in words:
                dict_of_words[count] = word
                count = count + 1
            logger.info("resultant dictionary is :%s",str(dict_of_words))
            return dict_of_words
    except Exception:
        logger.error("An Error Occured in base class")


class Child(Parent):
    """Child class inheriting parent class """
    def __init__(self,filename):
        self.filename=filename

    try:
        def write_into_newfile(self):
            """Used for string operations and writes result to new file"""
            new_name = str(uuid.uuid4())+".txt"
            words = []
            with open(self.filename, 'r',encoding='utf8') as file:
                contents=file.read()
                for line in file:
                    for word in line.split():
                        words.append(word)
            spliter_vowels = re.split('a|e|i|o|u|A|E|I|O|U', contents)
            with open(new_name, 'w', encoding='utf8') as new_file:
                new_file.writelines(spliter_vowels)
                new_file.write("\n After Capitalizing 3rd character of every word is :\n")
                for value in words:
                    if len(value) >= 3:
                        word = value[:2] + value[2].upper()
                        if len(value) > 3:
                            word= word + value[3:]
                        new_file.write(word + " ")
                    else:
                        new_file.write(value + " ")
                new_file.write("\n After Capitalizing 5th word is :\n")
                count = 1
                for value in words:
                    if count == 5:
                        count = count + 1
                        new_file.write(value.upper() + " ")
                    else:
                        count = count + 1
                        new_file.write(value + " ")
                new_file.write("\n After replacing space with hypen is :\n")
                replace_content = contents.replace(" ", '-')
                new_file.writelines(replace_content)
                new_file.write("\n After replacing new line with semicolon is :\n")
                replace_content = contents.replace("\n", ';')
                new_file.writelines(replace_content)
    except Exception:
        logger.error("Error occured in subclass")



if __name__=="__main__":
    try:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        file_handler = logging.FileHandler('logFile.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        child1=Child(sys.argv[1])
        logger.info(child1.filename)
        print(child1.prefix_count("to"))
        print(child1.suffix_count("ing"))
        print(child1.max_repeat_word())
        print(child1.palindrome())
        print(child1.to_unique_list())
        print(child1.to_dict())
        child1.write_into_newfile()
    except Exception:
        logger.error("Error occured in main")
