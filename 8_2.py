#!/usr/bin/env python
fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    fh = open('romeo.txt')
lst = list()
for line in fh:
	word = line.rstrip().split()
	for element in word:
         if element in lst:
             continue
         else:
             lst.append(element)
lst.sort()
print lst