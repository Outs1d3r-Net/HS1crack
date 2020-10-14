#!/usr/bin/env python2

#===> LIBRARIES
import hashlib
import hmac
import sys


#===> COLOR TABLE
#Red    = \033[91m
#Green  = \033[92m
#White  = \033[0m

#===> USAGE
if len(sys.argv) != 4:
    print "Usage: WORDLIST HMAC-SHA1 SALT"
    sys.exit(1)

#===> VARIABLES
w = sys.argv[1]
f = open(w, 'r')

hASH = sys.argv[2]
salt = sys.argv[3]

np = 1 #counter

#===> MAIN
for p in f:
    crackH = hmac.new(salt, p.strip('\n'), hashlib.sha1).hexdigest()
    if crackH == hASH:
        print "\n\n\033[1;92m [*] KEY FOUND !\033[1;91m ==> \033[0m",crackH,"\033[1;91m ==> \033[1;92m",p,"\033[0m"
        break
        sys.exit(0)
    else:
        print "\033[94mTrying...\t\033[91mHASH\t\033[0m=\t\033[0m",crackH,"\t\033[92mNUMBER\t\033[0m=\t\033[0m",np
        np += 1
