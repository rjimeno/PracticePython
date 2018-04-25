#!/usr/bin/env python3

import sys

primes = [int(line.rstrip()) for line in open(sys.argv[1])]

happy = [int(line.rstrip()) for line in open(sys.argv[2])]

happyAndPrime = [p for p in primes if p in happy]

print(happyAndPrime)
