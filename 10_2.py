#!/usr/bin/env python
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
counts=dict()
fh = open(fname)
lst = list()
for line in fh:
    if line.startswith('From '):
    	words = line.split()
    	str = words[5]
    	hour = str[0:str.find(":"):1]
    	#print hour
        counts[hour] = counts.get(hour, 0) + 1
for k, v in counts.items():
	lst.append((k,v))
lst.sort()
for v, k in lst:
    print v, k
#counts[time] = counts.get(time, 0) + 1
# print lst
                    #for name in name:
            	
        #	if name not in counts:
        	#	counts[name]=1
        	#else :
        	#	counts[name]=counts[name] + 1
#print counts
