#!/usr/bin/env python
from __future__ import print_function
import time
from fluxotron import Bridge, presets

bridge = Bridge(ip='10.0.0.42', app_name='testscript')
lights = bridge.get_lights()

## Set the lights to a jarring, eye-gouging 6500K (over 3 seconds)
for light in lights:
    print('Blinding you from %s' % light.name)
    light.set_kelvin(6500, secs=3)

time.sleep(5)

## Dim the lights for a movie, optionally turning them entirely off
for light in lights:
    print('Turning down %s' % light.name)
    light.movie_dim(off=True)

time.sleep(6)

## Set the lights to a sleepy 2000K
for light in lights:
    print('Immediately turning on %s at %dK' % (light.name,
                                                presets.CANDLE_LIGHT))
    light.torch(kelvin=presets.CANDLE_LIGHT, lum=127)

time.sleep(3)

## Switch in jarring fashion to 4500K (equivalent to clear a mid-afternoon sky)
for light in lights:
    print('Immediately switching to mid-afternoon light (%dK)' %
          presets.MID_AFTERNOON)
    light.set_kelvin(presets.MID_AFTERNOON)
