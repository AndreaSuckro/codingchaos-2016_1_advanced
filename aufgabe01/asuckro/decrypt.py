#!/usr/bin/python
import sys

key = list('chaostreffosnabrueck')
text = list(str(sys.argv[1])) #hope it is the first and only argument :D

#encode each character
i = 0
for c in text:
    print chr((ord(c) - 97 - ord(key[i%len(key)])-97)%26 + 97),
    i = i + 1
