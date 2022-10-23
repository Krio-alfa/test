from sys import path

path.append("..\\packages")

from packages.mysplit.mysplit_module import *

string = input('Input your text: ')

print(mysplit(string))
