HELIOTRON
=========

[![PyPI version](https://badge.fury.io/py/heliotron.png)](http://badge.fury.io/py/heliotron)

Heliotron is a simple library that talks to Philips Hue light bridges through
[a supported REST API][1]. It is currently a fairly rough work-in-progress.

Several use cases were the primary motivation for this library:

* I wanted a script that gradually changed color temperature of Philips Hue
  lighting on the same schedule as the popular [f.lux][2] utility. _(This is
  now available with the latest f.lux for Windows release.)_
* I'd like to switch on a subset of my lights around sunset/dusk, if they're
  not already on, so that I don't come home to a pitch dark apartment.
* The official Hue mobile apps won't let you store more than 3 active schedules
  on the bridge at a time, which is quite limited. This library provides the
  ability to write a simple script to switch or fade on a set of lights, and
  crontab it however you please.


License
-------

Heliotron is licensed under the [MIT License][3]. See the LICENSE file.

  [1]: http://developers.meethue.com/coreconcepts.html
  [2]: http://justgetflux.com
  [3]: http://en.wikipedia.org/wiki/MIT_License
