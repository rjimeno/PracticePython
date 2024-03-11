#!/usr/bin/env python3

import sys

primes = set([int(line.rstrip()) for line in open(sys.argv[1])])

happy = set([int(line.rstrip()) for line in open(sys.argv[2])])

happy_and_prime = primes.intersection(happy)  # [p for p in primes if p in happy]

for i in happy_and_prime:
    print(i)
