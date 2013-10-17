from util import RestObject

KELVIN_MIN = 2000
KELVIN_MED = 4500
KELVIN_MAX = 6500
MIRED_MIN = 500
MIRED_MED = 222
MIRED_MAX = 153
LUM_MIN = 0
LUM_MAX = 255


def kelvin_to_mired(kelvin):
    return int(1000000 / kelvin)


def secs_to_lsecs(secs):
    return secs * 10


class Light(RestObject):
    def __init__(self, id=None, name=None, bridge=None, color_temp=None,
                 trans_time=None):
        self.id = id
        self.name = name
        self.bridge = bridge
        self.rest_group = 'lights'
        self.color_temp = color_temp
        self.trans_time = trans_time

        if (self.color_temp):
            self.color_mired = kelvin_to_mired(self.color_temp)

    def set_kelvin(self, kelvin, secs=0):
        body = {'on': True,
                'ct': kelvin_to_mired(kelvin),
                'transitiontime': secs_to_lsecs(secs)}
        self.put('state', body)

    def movie_dim(self, secs=5, off=False):
        body = {'on': True and not off,
                'transitiontime': secs_to_lsecs(secs)}
        self.put('state', body)

    def torch(self, kelvin=KELVIN_MED, secs=0, lum=LUM_MAX):
        self.put('state', {'on': True,
                           'ct': kelvin_to_mired(kelvin),
                           'bri': lum,
                           'transitiontime': secs_to_lsecs(secs)})
