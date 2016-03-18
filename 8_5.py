#!/usr/bin/env python
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst = list()
for line in fh:
	#count = count +1
    if line.startswith('From '):
        ad = line.rstrip().split()
        count = count +1
        print ad[1]
print 'There were', count, 'lines in the file with From as the first word'
	#word = line.rstrip().split()


	#for element in word:
     #    if element in lst:
      #       continue
       #  else:
        #     lst.append(element)
#lst.sort()
#print line