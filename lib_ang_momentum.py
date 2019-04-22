#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Python library to calculate the total angular momentum of each planetary system
in our solar system.

Written by: Viranga Perera & Ankit Barik

Main calculation:
Need to add three angular momentums for each planetary system:
1. Due to the spin of the planet
2. Due to the spin of the moon(s)
3. Due to the orbit(s) of the moon(s)

Notes:
So far, only included at most the largest 4 moons of a planetary system
For Phobos, Deimos, Iapetus, Dione, Titania, Oberon, Triton & Proteus
Using a normalized moment of inertia of 0.4 (check if there are better numbers)

"""

# Python imports
from numpy import pi, arange, array

# Function to calculate angular rate (rad/s) for either spin or orbital periods
def AngularRate(Period, Units):

    Seconds_in_Day = 86400
    Seconds_in_Hour = 3600

    # Day is an Earth day
    if Units == "Days":
        # Convert rotation period from days to seconds
        Period = Seconds_in_Day * Period
    elif Units == "Hours":
        # Convert rotation period from hours to seconds
        Period = Seconds_in_Hour * Period

    return (2 * pi) / Period


# Define Planetary System Class
class PlanetarySystem:
    def __init__(self, planet, *moons):
        self.planet              = planet
        self.planet_ang_momentum = self.planet.SpinAngMomentum()
        self.moons               = array(moons).flatten()
        self.moons_ang_momentum  = 0.

        if len(self.moons) > 0:
            for k in range(len(self.moons)):
                self.moons_ang_momentum += self.moons[k].SpinAngMomentum() \
                                         + self.moons[k].OrbitAngMomentum()

        self.total_ang_momentum = self.planet_ang_momentum \
                                  + self.moons_ang_momentum

# Define Planet Class
class planet:
    # Instance Attributes
    def __init__(self, name, mass, radius, norm_moment_inertia, rotational_rate):

        # Attributes that should be updated
        self.name                = name                 # Planet name
        self.mass                = mass                 # Mass (kg)
        self.radius              = radius               # Radius (m)
        self.norm_moment_inertia = norm_moment_inertia  # Normalized moment of inertia (unitless)
        self.rotational_rate     = rotational_rate      # Rotation rate (rad/s)

    def SpinAngMomentum(self):
        return self.norm_moment_inertia * self.mass * self.radius**2  * self.rotational_rate

# Define Moon Class (Inherits from Planet Class)
class moon(planet):
    # Instance Attributes
    def __init__(self, name, mass, radius, norm_moment_inertia, rotational_rate, distance, orbital_rate):

        # Attributes that are inherited
        planet.__init__(self, name, mass, radius, norm_moment_inertia, rotational_rate)

        # Attributes that should be updated
        self.distance     = distance                    # Semi-major axis, average distance from planet (m)
        self.orbital_rate = orbital_rate                # Orbital rate (rad/s)

    def OrbitAngMomentum(self):
        return self.mass * self.distance**2 * self.orbital_rate
