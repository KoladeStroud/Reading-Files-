# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from logging.handlers import DEFAULT_SOAP_LOGGING_PORT


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        readtext = f.read()cd DEFAULT_SOAP_LOGGING_PORTdcd
        return readtext


def count_words():
    text = read_file_content("C:\Users\LENOVO\Desktop\htmlprojects\story.txt")
    # [assignment] Add your code here
    textlist = text.split(" ")
    for i in textlist:
        dictionary = {i: textlist.count(i)}
        print(dictionary)

count_words()