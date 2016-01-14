#!/usr/bin/python
from __future__ import print_function
import sys

key = list('chaostreffosnabrueck')
text = list(str(sys.argv[1])) #hope it is the first and only argument :D

#encode each character
for i in range(0,len(text)):
    print (chr((ord(text[i]) - 97 + ord(key[i%len(key)])-97)%26 + 97),end='')
