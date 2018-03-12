#!/usr/bin/env python3

from __future__ import print_function
import sys
import time
from sys import stdout
from time import sleep

#messages = [
#    'announce route 100.10.0.0/24 next-hop self',
#    'announce route 200.20.0.0/24 next-hop self',
#]

next_hop="10.247.250.122"

for x in range (1, 100):
    for y in range (1, 110):
        sys.stdout.write("announce route "+str(x)+"."+str(y)+".0.0/24 next-hop "+next_hop +'\n')
        sys.stdout.flush()


sleep(5) 

#Iterate through messages
#for message in messages:
#    stdout.write(message + '\n')
#    stdout.flush()
#    sleep(1)

#Loop endlessly to allow ExaBGP to continue running
while True:
    sleep(1)
