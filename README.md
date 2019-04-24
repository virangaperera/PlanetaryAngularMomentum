# Planetary Angular Momentum

This a Python script that calculates and plots angular momenta of planetary systems for a particular star system. The default is our solar system. This script was written by Viranga Perera and Ankit Barik. This is a free software. It can be used, modified and redistributed under the terms of the GNU GPL (v3) open source licence.

## Introduction

Quotes from the literature:
* "The angular momentum of the Earth-Moon system is...unusually high"
* "The high angular momentum of the Earth-Moon system"
* "The anomalously large angular momentum to the Earth-Moon system"

The total angular momentum of the Earth-Moon system is often used as an argument for the giant impact origin of the Moon. The total angular momentum of a planetary system includes angular momentum: 
1. Due to the spin of the planet
2. Due to the spin of the moon(s)
3. Due to the orbit(s) of the moon(s)

This script was mainly written to demonstrate that the total angular momentum of the Earth-Moon system is not unusually higher than the other planetary systems in our solar system (see figure).

<p align="center">
<img src="https://github.com/virangaperera/PlanetaryAngularMomentum/blob/master/Plots/Total_Angular_Momentum_Comparison.png" width="612" height="360" align="middle">
</p>

Yet, there is something special about the angular momentum of the Earth-Moon system. Of the total angular momentum of the system, most of the angular momentum is due to the Moon (see figure).

<p align="center">
<img src="https://github.com/virangaperera/PlanetaryAngularMomentum/blob/master/Plots/Planet_Moons_Angular_Momentum_Comparison.png" width="612" height="360" align="middle">
</p>

For the other planetary systems in our solar system most of the angular momentum resides in the planet. This point has already been made by [MacDonald (1966)](https://link.springer.com/chapter/10.1007/978-1-4684-8401-4_12), yet today it is often true that the angular momentum arguement is not presented properly.

It is still true that the Moon likely formed from a giant impact, but it is important to understand that it is not the total but rather the fraction of angular momentum that is in the planet vs. the moon(s) that may indicate a giant impact formation scenario. A higher fraction of angular momentum in the moon(s) may indicate a giant impact origin, whereas a higher fraction in the planet may suggest a more accretionary-type origin of the moon(s).

## Script Inputs
All necessary planetary data for planets in our solar system are included in the *config.ini* file. If you would like to use this script for exoplanets, please edit the *config.ini* file as needed.

## Script Usage
To run this script, please make sure to have [Python](https://wiki.python.org/moin/BeginnersGuideinstalled) installed on your computer along with the [NumPy](https://www.numpy.org/) and [Matplotlib](https://matplotlib.org/) libraries. Please navigate to the PlanetaryAngularMomentum directory using a Terminal window (once you have either downloaded or cloned the script from Github). Then type the following:
```bash
python main.py
```

## Contributing
We would love for you to improve this script. Please let us know if you have sugguestions and/or questions.

Contact info:
Viranga Perera (vperera1@jhu.edu) and Ankit Barik (abarik@jhu.edu)

## Script License
[GNU General Public License v3.0](http://www.gnu.org/licenses/gpl-3.0.en.html)
