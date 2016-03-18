#!/usr/bin/env python
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
z = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count +1
    x = line.find('0')
    y = line[x:]
    print float(y)
    z = z + float(y)
    #print count
    

print "Done"
print count
print z
print z/count