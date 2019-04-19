#!/usr/bin/env python

# -*- coding: utf-8 -*-
"""
Python (v3.5.2) script to calculate the total angular momentum of each planetary system
in our solar system.

Written by: Viranga Perera & Ankit Barik
Last modified: April 19, 2019 (by VP)

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
import matplotlib.pyplot as plt

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


########## MAIN  ##########

# Input planet properties: name(string), mass(kg), radius(m), norm_moment_inertia(no units), rotational_rate(days, hours)
# Input moon properties: name(string), mass(kg), radius(m), norm_moment_inertia(no units),
#                       rotational_rate(days, hours), distance(m), orbital_rate(days, hours)

if __name__ == '__main__':

    MercurySystem = PlanetarySystem(planet('Mercury', 3.3011e23, 2439.7e3, 0.346, AngularRate(58.646, "Days")))

    VenusSystem   = PlanetarySystem(planet('Venus', 4.8675e24, 6051.8e3, 0.33, AngularRate(243.025, "Days")))

    EarthSystem   = PlanetarySystem(planet('Earth', 5.97237e24, 6371.0e3, 0.3307, AngularRate(0.99726968, "Days")), \
                    moon('Moon', 7.342e22, 1737.1e3, 0.3929, AngularRate(27.321661, "Days"), 384399e3, AngularRate(27.321661, "Days")))

    MarsSystem    = PlanetarySystem(planet('Mars', 6.4171e23, 3389.5e3, 0.3662, AngularRate(1.025957, "Days")), \
                    [moon('Phobos', 1.0659e16, 11.2667e3, 0.4, AngularRate(0.31891023, "Days"), 9376e3, AngularRate(0.31891023, "Days")), \
                    moon('Deimos', 1.4762e15, 6.2e3, 0.4, AngularRate(1.263, "Days"), 23463.2e3, AngularRate(1.263, "Days"))])

    JupiterSystem = PlanetarySystem(planet('Jupiter', 1.8982e27, 69911e3, 0.254, AngularRate(9.925, "Hours")), \
                    [moon('Io', 8.931938e22, 1821.6e3, 0.3755, AngularRate(1.769137786, "Days"), 421700e3, AngularRate(1.769137786,"Days")), \
                    moon('Europa', 4.799844e22, 1560.8e3, 0.346, AngularRate(3.551181, "Days"), 670900e3, AngularRate(3.551181, "Days")), \
                    moon('Ganymede', 1.4819e23, 2634.1e3, 0.3105, AngularRate(7.15455296, "Days"), 1070400e3, AngularRate(7.15455296, "Days")), \
                    moon('Callisto', 1.075938e23, 2410.3e3, 0.359, AngularRate(16.6890184, "Days"), 1882700e3, AngularRate(16.6890184, "Days"))])

    SaturnSystem  = PlanetarySystem(planet('Saturn', 5.6834e26, 58232e3, 0.210, AngularRate(10.56, "Hours")), \
                    [moon('Titan', 1.3452e23, 2574.73e3, 0.3414, AngularRate(15.945, "Days"), 1221870e3, AngularRate(15.945, "Days")), \
                    moon('Rhea', 2.306518e21, 763.8e3, 0.3911, AngularRate(4.518212, "Days"), 527108e3, AngularRate(4.518212, "Days")), \
                    moon('Iapetus', 1.805635e21, 734.5e3, 0.4, AngularRate(79.3215, "Days"), 3560820e3, AngularRate(79.3215, "Days")), \
                    moon('Dione', 1.095452e21, 561.4e3, 0.4, AngularRate(2.736915, "Days"), 377396e3, AngularRate(2.736915, "Days"))])

    UranusSystem  = PlanetarySystem(planet('Uranus', 8.6810e25, 25362e3, 0.23, AngularRate(0.71833, "Days")), \
                    [moon('Titania', 3.527e21, 788.4e3, 0.4, AngularRate(8.706234, "Days"), 435910e3, AngularRate(8.706234, "Days")), \
                    moon('Oberon', 3.014e21, 761.4e3, 0.4, AngularRate(13.463234, "Days"), 583520e3, AngularRate(13.463234, "Days")), \
                    moon('Umbriel', 1.172e21, 584.7e3, 0.4, AngularRate(4.144, "Days"), 266000e3, AngularRate(4.144, "Days")), \
                    moon('Ariel', 1.353e21, 578.9e3, 0.4, AngularRate(2.520, "Days"), 191020e3, AngularRate(2.520, "Days"))])

    NeptuneSystem = PlanetarySystem(planet('Neptune', 1.02413e26, 24622e3, 0.23, AngularRate(0.6713, "Days")), \
                    [moon('Triton', 2.14e22, 1353.4e3, 0.4, AngularRate(5.876854, "Days"), 354759e3, AngularRate(5.876854, "Days")), \
                    moon('Proteus', 4.4e19, 210e3, 0.4, AngularRate(1.12231477, "Days"), 117647e3, AngularRate(1.12231477, "Days"))])

    # Make a list of planetary systems
    PlanetarySystemsList = [MercurySystem, VenusSystem, EarthSystem, MarsSystem, JupiterSystem, SaturnSystem, UranusSystem, NeptuneSystem]

    # Setup data for plotting
    total_ang_momentum_list = []
    planet_ang_momentum_list = []
    moons_ang_momentum_list = []
    planet_names_list = []

    for system in PlanetarySystemsList:

        total_ang_momentum_list.append(system.total_ang_momentum)
        planet_ang_momentum_list.append(system.planet_ang_momentum)
        moons_ang_momentum_list.append(system.moons_ang_momentum)
        planet_names_list.append(system.planet.name)

    # Figure setup
    N = len(PlanetarySystemsList)
    index = arange(N)       # x locations for groups
    
    # Figure 1
    plt.figure(1)
    width = 0.35            # width of bars

    p1 = plt.bar(index, total_ang_momentum_list, width, color='#006ddb', edgecolor='k')

    plt.ylabel('Total Angular Momentum ($kg \cdot m^2 / s$)', fontweight='bold', fontsize=13)
    plt.xlabel('Planetary Systems', fontweight='bold', fontsize=13)
    plt.xticks(index, planet_names_list, fontsize=10)
    plt.yscale('log')
    plt.show()

    # Save current plot to eps
    plotName = 'Total_Angular_Momentum_Comparison.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()

    # Figure 2
    fig, ax = plt.subplots()
    width = 0.35            # width of bars

    p1 = ax.bar(index, planet_ang_momentum_list, width, color='#006ddb', edgecolor='k')
    p2 = ax.bar(index + width, moons_ang_momentum_list, width, color='#db6d00', edgecolor='k')

    ax.set_ylabel('Angular Momentum ($kg \cdot m^2 / s$)', fontweight='bold', fontsize=13)
    ax.set_xlabel('Planetary Systems', fontweight='bold', fontsize=13)
    ax.set_xticks(index + width / 2)
    ax.set_xticklabels(planet_names_list, fontsize=10)
    ax.set_yscale('log')
    ax.legend((p1[0], p2[0]), ('Planet', 'Moon(s)'))
    plt.show()

    # Save current plot to eps
    plotName = 'Planet_Moons_Angular_Momentum_Comparison.eps'
    plt.savefig(plotName, bbox_inches='tight')
    plt.close()