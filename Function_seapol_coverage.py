#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:11:13 2024

@author: cstoll
"""

import numpy as np
import matplotlib.pyplot as plt

def seapol_coverage(N1, N2, N3, N4):
    """
    Generate and plot Seapol sampling coverage for North, South, West, Southeast, and Southwest directions.

    Parameters:
    - N1, N2, N3, N4: Azimuth angle ranges for North direction.
    - Input values for ranges that are wanted to be seen by the radar, from smallest to greatest value
    - example (0,90,225,360), in this example 0-90 degrees will be seen in the north direction 
    - and 225-360 will be seen in the north direction
    """

    # Define azimuth angles from 0 to 360 degrees with a step of 1 degree
    az = np.arange(0, 361, 1)

    # Define hours of sampling in different directions
    HoursN = 422
    HoursS = 418
    HoursW = 134
    HoursSE = 19
    HoursSW = 71

    # Create an array to store the sample data for each azimuth angle
    Sample = np.zeros(361)

    # Fill the sample array for North direction
    Sample[N1:N2 + 1] = HoursN
    Sample[N3:N4 + 1] += HoursN

    # Fill the sample array for South direction
    Sample[N1 + 180:N2 + 181] += HoursS
    Sample[N3 - 180:N4 - 179] += HoursS

    # Fill the sample array for West direction
    Sample[N1 + 180:N2 - 90] += HoursW
    Sample[N3 - 90:N4 + 1] += HoursW

    # Fill the sample array for Southeast direction
    Sample[N1 + 135:N2 + 135 + 1] += HoursSE
    Sample[N3 - 225:N4 - 224] += HoursSE

    # Fill the sample array for Southwest direction
    Sample[N1 + 180:N2 + 225] += HoursSW
    Sample[N3 - 135:N4 - 180] += HoursSW

    # Calculate total hours of sampling
    HoursTOT = HoursSE + HoursN + HoursS + HoursW + HoursSW

    # Create arrays for radius and coverage based on the sample data
    radius = np.arange(0, 151, 50)
    coverage = np.tile(Sample, (len(radius), 1))

    # Create a polar plot using Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    h1 = ax.pcolormesh(np.radians(az), radius, coverage / HoursTOT, cmap='plasma', vmin=0.3, vmax=1.0)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rlabel_position(180)
    fig.colorbar(h1)
    ax.set_title('Seapol Sampling by Azimuth', fontsize=18, weight='bold', loc='center')



