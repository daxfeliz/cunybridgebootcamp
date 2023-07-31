#!/usr/bin/env python
import numpy as np
import sys

def stellar_r(mass):
    if mass<1: #smaller stars than sun
        starR=mass**0.8
    if mass>1:#larger stars than sun
        starR=mass**0.57
    if mass==1: #stars with equal mass of sun
        starR=1
    return starR

if __name__ == "__main__":
    print (stellar_radius(float(sys.argv[1]))) #mass
