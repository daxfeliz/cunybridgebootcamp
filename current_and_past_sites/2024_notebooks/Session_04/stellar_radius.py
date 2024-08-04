#!/usr/bin/env python
import numpy as np
import sys

def stellar_r(mass):
    """
    Calculate the radius of a star based on its mass relative to the Sun.

    The radius is estimated using different scaling laws depending on whether
    the star's mass is smaller than, larger than, or equal to the Sun's mass.

    Parameters:
    mass (float): The mass of the star in solar masses. 

    Returns:
    float: The estimated radius of the star in solar radii.

    Notes:
    - For stars with mass less than 1 solar mass, the radius is calculated as
      mass raised to the power of 0.8.
    - For stars with mass greater than 1 solar mass, the radius is calculated as
      mass raised to the power of 0.57.
    - For stars with mass equal to 1 solar mass, the radius is set to 1 solar radius.
    """
    if mass<1: #smaller stars than sun
        starR=mass**0.8
    if mass>1:#larger stars than sun
        starR=mass**0.57
    if mass==1: #stars with equal mass of sun
        starR=1
    return starR

if __name__ == "__main__":
    print (stellar_radius(float(sys.argv[1]))) #mass
