#!/usr/bin/python
import sys
import subprocess
import time

password = ''
chars = map(chr, range(65, 91))
fettig = False

while not fettig:
    for c in chars:
        start = time.time()
        a = subprocess.call(['../crypto',str(password)+str(c)])
        end = time.time()
        if a == 2:
            fettig = True
            break
        if end-start > 0.1*(len(password)+1):
            password = password + c

print password
