#!/usr/bin/env python
import numpy as np
import sys

import numpy as np

def stellar_r(mass):
    """
    Calculate the radius of a star based on its mass relative to the Sun.

    The radius is estimated using different scaling laws depending on whether
    the star's mass is smaller than, larger than, or equal to the Sun's mass.

    Parameters:
    mass (float/int/list/array): The mass of the star in solar masses. 

    Returns:
    float/int/list/array: The estimated radius of the star in solar radii.

    Notes:
    - For stars with mass less than 1 solar mass, the radius is calculated as
      mass raised to the power of 0.8.
    - For stars with mass greater than 1 solar mass, the radius is calculated as
      mass raised to the power of 0.57.
    - For stars with mass equal to 1 solar mass, the radius is set to 1 solar radius.
    """
    mass = np.array(mass, dtype=float)  # ensures we can do element-wise operations

    starR = np.empty_like(mass)

    # Smaller stars than the Sun
    starR[mass < 1] = mass[mass < 1] ** 0.8

    # Larger stars than the Sun
    starR[mass > 1] = mass[mass > 1] ** 0.57

    # Stars with equal mass to the Sun
    starR[mass == 1] = 1.0

    # If the input was a single number, return a scalar
    if starR.size == 1:
        return float(starR)
    return starR


if __name__ == "__main__":
    print (stellar_radius(float(sys.argv[1]))) #mass
