#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python library for Planetary_Angular_Momentum.py
"""

# Python imports
from numpy import pi, arange, array

# Function to calculate angular rate (rad/s) for either spin or orbital periods
def AngularRate(Period):

    # Number of seconds in a day
    Seconds_in_Day = 86400

    # Convert rotation period from days to seconds
    Period = Seconds_in_Day * Period

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
