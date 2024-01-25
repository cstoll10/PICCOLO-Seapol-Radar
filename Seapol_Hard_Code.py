#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 07:01:46 2024

@author: cstoll


"""

import numpy as np
import matplotlib.pyplot as plt

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

# Define azimuth angle ranges for North direction
N1 = 0
N2 = 90
N3 = 225
N4 = 360

# Fill the sample array for North direction
Sample[N1:N2 + 1] = HoursN
Sample[N3 + 1:N4 + 1] += HoursN

# Define azimuth angle ranges for South direction
S1 = 45
S2 = 180
S3 = 180
S4 = 270

# Fill the sample array for South direction
Sample[S1:S2 + 1] += HoursS
Sample[S3 + 1:S4] += HoursS

# Define azimuth angle ranges for West direction
W1 = 135
W2 = 360
W3 = 0
W4 = 0

# Fill the sample array for West direction
Sample[W1:W2 + 1] += HoursW
Sample[W3:W4 + 1] += HoursW

# Define azimuth angle ranges for Southeast direction
SE1 = 0
SE2 = 90
SE3 = 90
SE4 = 225

# Fill the sample array for Southeast direction
Sample[SE1:SE2] += HoursSE
Sample[SE3:SE4 + 1] += HoursSE

# Define azimuth angle ranges for Southwest direction
SW1 = 90
SW2 = 100
SW3 = 100
SW4 = 315

# Fill the sample array for Southwest direction
Sample[SW1:SW2] += HoursSW
Sample[SW3:SW4] += HoursSW

# Calculate total hours of sampling
HoursTOT = HoursN + HoursS + HoursW + HoursSE + HoursSW

# Create arrays for radius and coverage based on the sample data
radius = np.arange(0, 151, 50)
coverage2 = np.tile(Sample, (len(radius), 1))

# Create a polar plot using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
h1 = ax.pcolormesh(np.radians(az), radius, coverage2 / HoursTOT, cmap='plasma', vmin=0.4, vmax=1.0)
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_rlabel_position(180)
fig.colorbar(h1)
ax.set_title('Seapol Sampling by Azimuth', fontsize=18, weight='bold', loc='center')

