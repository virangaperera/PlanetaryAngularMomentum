# Planetary Angular Momentum

Python script to calculate and plot the angular momentum of planetary systems for a particular star system. This script is written by Viranga Perera and Ankit Barik. This is a free software. It can be used, modified and redistributed under the terms of the GNU GPL v3 licence.

## Foreword
The total angular momentum of the Earth-Moon system is often used as an argument for the giant impact origin of the Moon. This script was written to demonstrate that the total angular momentum of the Earth-Moon system is not unusually higher than the other planetary systems in our solar system. Yet, there is something special about the angular momentum of the Earth-Moon system. Of the total angular momentum of the system, most of the angular momentum is due to the Moon. This is not like the other planets in our solar system, where most of the angular momentum of a particular planetary system is in the planet. The Moon was still likely formed after a giant impact but it is important to understand that it is not the total but rather the fraction of angular momentum that is in the planet vs. the moon(s) that may indicate a giant impact formed the moon(s). A higher fraction of angular momentum in the moon(s) may indicate a giant impact origin, whereas a higher fraction in the planet may suggest a more accretionary-type origin of the moon(s).

![alt tag](https://raw.github.com/magic-sph/magic/master/doc/sphinx/.themes/magic/static/logo.png)

## Outputs
This script will generate two figures (PDF files). One will plot the total angular momentum for each planetary system. The total angular momentum will include: 
1. Due to the spin of the planet
2. Due to the spin of the moon(s)
3. Due to the orbit(s) of the moon(s)

The other plot will compare the angular momenta of the planet and the moon(s).

## Inputs
All necessary planetary data for planets in our solar system are included in the *config.ini* file. If you would like to use this script for exoplanets please change the *config.ini* file as needed.

## Usage
To run this script, navigate to the PlanetaryAngularMomentum directory using a Terminal. Then type the following:
```bash
python main.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU General Public License v3.0](http://www.gnu.org/licenses/gpl-3.0.en.html)
