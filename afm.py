#!/bin/python

from __future__ import division
import time

# This script generates a wordlist with all the possible Greek tax record reference numbers

def add_9th(x):          # adds the 9th digit to an 8-digit number
    a = int(x[0])*256
    b = int(x[1])*128
    c = int(x[2])*64
    d = int(x[3])*32
    e = int(x[4])*16
    f = int(x[5])*8
    g = int(x[6])*4
    h = int(x[7])*2
    i = (a+b+c+d+e+f+g+h)/11
    return x+str(i)[-1:]

def pre_afm():          # calculates every possible 8-digit number
    tmp = []
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        for g in range(0, 10):
                            for h in range(0, 10):
                                for a in range(0, 10):
                                    tmp.append(str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(a))
    return tmp

def AFM(l):
    tmp = []
    for i in l:
        tmp.append(add_9th(i))
    return tmp


def write_out(x):
    mylist = file('afm_list_%s.txt' % time.strftime('%d-%m-%Y_%H:%M'), 'w')
    mylist.write(x)
    mylist.close
    raw_input("\n\nAll done! Press enter to exit")
    exit()


list_8_bits = pre_afm()
afm_list = AFM(list_8_bits)

our_list = "\n".join(afm_list)
write_out(our_list)
