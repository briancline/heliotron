from util import RestObject
from light import Light


class Bridge(object):
    def __init__(self, ip, app_name):
        self.ip = ip
        self.app_name = app_name
        self.base_url = 'http://%s/api/%s' % (self.ip, self.app_name)

    def get_lights(self):
        lights = RestObject(self).get('lights').json()
        return [Light(id=light_id, name=light['name'], bridge=self)
                for light_id, light in lights.iteritems()]
