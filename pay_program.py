#!/usr/bin/env python

try:
    inp=input('Enter Hours:')
    hours=float(inp)
    inp=input('Enter Rate:')
    rate=float(inp)
except:
    print ('please enter numeric input')
    quit()
if hours > 40:
    pay=40 * rate + ((hours-40) * (rate * 1.5))
    print 'Pay:',pay
else:
    pay=hours * rate
    print pay





