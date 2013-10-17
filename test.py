#!/usr/bin/env python
from __future__ import print_function
import time
from datetime import datetime
from heliotron import Bridge, presets
from astral import Astral

## Set up our timezone by feeding in the nearest major city, and then a
## more precise latitude/longitude (optional), to get the most accurate
## sunrise/sunset times as is possible
astral = Astral()
astral.solar_depression = 'civil'  # 6 degrees below horizon
city = astral.geocoder['Dallas']
city.latitude = 32.9614
city.longitude = -96.8259
sun = city.sun(date=datetime.now(), local=True)

print(city)
print('Dawn:    %s' % str(sun['dawn']))
print('Sunrise: %s' % str(sun['sunrise']))
print('Sunset:  %s' % str(sun['sunset']))
print('Dusk:    %s' % str(sun['dusk']))

bridge = Bridge(ip='10.0.0.42', app_name='testscript')
lights = bridge.get_lights()

## Set the lights to a jarring, eye-gouging 6500K (over 3 seconds)
print('Blinding you...')
for light in lights:
    print('- from %s' % light.name)
    light.set_kelvin(6500, secs=3)

time.sleep(5)

## Dim the lights for a movie, optionally turning them entirely off
print('Turning down lights...')
for light in lights:
    print('- at %s' % light.name)
    light.movie_dim(off=True)

time.sleep(6)

## Set the lights to a sleepy 2000K
print('Immediate %dK switch-on...' % presets.CANDLE_LIGHT)
for light in lights:
    print('- at %s' % light.name)
    light.torch(kelvin=presets.CANDLE_LIGHT, lum=127)

time.sleep(3)

## Switch in jarring fashion to 4500K (equivalent to clear a mid-afternoon sky)
print('Jarring temperature change to %dK...' % presets.MID_AFTERNOON)
for light in lights:
    print('- at %s' % light.name)
    light.set_kelvin(presets.MID_AFTERNOON)
