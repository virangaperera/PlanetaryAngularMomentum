# Planetary Angular Momentum

Python script to calculate and plot angular momenta of planetary systems for a particular star system. The default is our solar system. This script is written by Viranga Perera and Ankit Barik. This is a free software. It can be used, modified and redistributed under the terms of the GNU GPL v3 licence.

## Introduction
The total angular momentum of the Earth-Moon system is often used as an argument for the giant impact origin of the Moon. The total angular momentum of a planetary system includes angular momentum: 
1. Due to the spin of the planet
2. Due to the spin of the moon(s)
3. Due to the orbit(s) of the moon(s)

This script was mainly written to demonstrate that the total angular momentum of the Earth-Moon system is not unusually higher than the other planetary systems in our solar system (see figure).

<img src="https://github.com/virangaperera/PlanetaryAngularMomentum/blob/master/Plots/Total_Angular_Momentum_Comparison.png" width="340" height="200">

Yet, there is something special about the angular momentum of the Earth-Moon system. Of the total angular momentum of the system, most of the angular momentum is due to the Moon (see figure).

<img src="https://github.com/virangaperera/PlanetaryAngularMomentum/blob/master/Plots/Planet_Moons_Angular_Momentum_Comparison.png" width="340" height="200">

This is not like the other planetary systems in our solar system, where most of the angular momentum resides in the planet. It is still true that the Moon was likely formed by a giant impact, but it is important to understand that it is not the total but rather the fraction of angular momentum that is in the planet vs. the moon(s) that may indicate a giant impact formation scenario. A higher fraction of angular momentum in the moon(s) may indicate a giant impact origin, whereas a higher fraction in the planet may suggest a more accretionary-type origin of the moon(s).

## Script Inputs
All necessary planetary data for planets in our solar system are included in the *config.ini* file. If you would like to use this script for exoplanets, please edit the *config.ini* file as needed.

## Script Usage
To run this script, please make sure to have Python installed on your computer along with the *numpy* and *matplotlib* libraries. Please navigate to the PlanetaryAngularMomentum directory using a Terminal window (once you have either downloaded or cloned the script from Github). Then type the following:
```bash
python main.py
```

## Contributing
We would love for you to improve this script. Please let us know if you have sugguestions and/or questions.

Contact info:
Viranga Perera (vperera1@jhu.edu) and Ankit Barik (abarik@jhu.edu)

## Script License
[GNU General Public License v3.0](http://www.gnu.org/licenses/gpl-3.0.en.html)
