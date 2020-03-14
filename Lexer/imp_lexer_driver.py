import sys
from imp_lexer import *

if __name__ == '__main__':
    file = open("filename.txt")
    characters = file.read()
    file.close()
    tokens = imp_lex(characters)
    for token in tokens:
        print (token)
