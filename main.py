#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import numpy as np
import matplotlib.pyplot as plt
try:
    import configparser as CoPa
except ImportError:
    import ConfigParser as CoPa
import json
from lib_ang_momentum import *

param_file  = 'config.ini'
num_planets = 8

total_ang_momentum_list = []
planet_ang_momentum_list = []
moons_ang_momentum_list = []
planet_names_list = []

# Get data from parameter file
 
parser = CoPa.ConfigParser()
parser.read(param_file)

for plIter in range(1,num_planets+1):
    planet_id = 'Planet'+str(plIter)

    name                = parser.get(planet_id,'name')
    mass                = parser.getfloat(planet_id,'mass')
    norm_moment_inertia = parser.getfloat(planet_id,'norm_moment_inertia')
    radius              = parser.getfloat(planet_id,'radius')
    rotation_period     = parser.getfloat(planet_id,'rotation_period')
    rotational_rate     = AngularRate(rotation_period, "Days")

    thisPlanet = planet(name, mass, radius, norm_moment_inertia, rotational_rate)
    moons = []
    
    try:
        moon_list = json.loads(parser.get(planet_id, 'moons'))
    except:
        moon_list = []
        pass

    if len(moon_list) > 0:
        for k in range(len(moon_list)):
            locals().update(moon_list[k])
            rotational_rate = AngularRate(rotation_period, "Days")
            orbital_rate    = AngularRate(orbital_period, "Days")
            thisMoon = moon(name, mass, radius, norm_moment_inertia, \
                            rotational_rate, distance, orbital_rate) 
            moons.append(thisMoon)

    
    thisSystem = PlanetarySystem(thisPlanet,moons)

    total_ang_momentum_list.append(thisSystem.total_ang_momentum)
    planet_ang_momentum_list.append(thisSystem.planet_ang_momentum)
    moons_ang_momentum_list.append(thisSystem.moons_ang_momentum)
    planet_names_list.append(thisSystem.planet.name)

#############
#   Plotting
#############

# Figure setup
index = arange(num_planets)       # x locations for groups

# Figure 1
plt.figure(figsize=(16,9))
width = 0.35            # width of bars

p1 = plt.bar(index, total_ang_momentum_list, width, color='#006ddb', edgecolor='k')

plt.ylabel('Total Angular Momentum ($kg \cdot m^2 / s$)', fontweight='bold', fontsize=30)
plt.xlabel('Planetary Systems', fontweight='bold', fontsize=30)
plt.xticks(index, planet_names_list, fontsize=20)
plt.yscale('log')
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.show()

# Save current plot to pdf
#plotName = 'Total_Angular_Momentum_Comparison.pdf'
#plt.savefig(plotName, bbox_inches='tight')
#plt.close()

# Figure 2
fig, ax = plt.subplots(figsize=(16,9))
width = 0.35            # width of bars

p1 = ax.bar(index, planet_ang_momentum_list, width, color='#006ddb', edgecolor='k')
p2 = ax.bar(index + width, moons_ang_momentum_list, width, color='#db6d00', edgecolor='k')

ax.set_ylabel('Angular Momentum ($kg \cdot m^2 / s$)', fontweight='bold', fontsize=30)
ax.set_xlabel('Planetary Systems', fontweight='bold', fontsize=30)
ax.set_xticks(index + width / 2)
ax.set_xticklabels(planet_names_list, fontsize=20)
ax.set_yscale('log')
ax.legend((p1[0], p2[0]), ('Planet', 'Moon(s)'),fontsize=30)
plt.tick_params(labelsize=20)
plt.tight_layout()
plt.show()

# Save current plot to pdf
#plotName = 'Planet_Moons_Angular_Momentum_Comparison.pdf'
#plt.savefig(plotName, bbox_inches='tight')
#plt.close()
