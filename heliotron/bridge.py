from heliotron.util import RestObject
from heliotron.light import Light


class Bridge(object):
    def __init__(self, ip, app_name):
        self.ip = ip
        self.app_name = app_name
        self.base_url = 'http://%s/api/%s' % (self.ip, self.app_name)

    def get_lights(self):
        lights = RestObject(bridge=self).get('lights').json()
        return [Light(light_id=light_id, name=light['name'], bridge=self)
                for light_id, light in lights.iteritems()]
