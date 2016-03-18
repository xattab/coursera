#!/usr/bin/env python
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
counts=dict()
fh = open(fname)
lst = list()
for line in fh:
    if line.startswith('From '):
        ad = line.rstrip().split()
        name = ad[1].split()
       # print name
        for name in name:
        	if name not in counts:
        		counts[name]=1
        	else :
        		counts[name]=counts[name] + 1
#print counts
maxval = None
maxkee = None
for kee,val in counts.items() :
	if maxval == None : maxval = val
	if maxval < val : 
		maxval = val
		maxkee = kee
print maxkee, maxval