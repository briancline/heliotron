#from __future__ import print_function
from requests import get, put
import json


class RestObject(object):
    def __init__(self, bridge=None):
        self.id = ''
        self.rest_group = 'unknown'
        self.bridge = bridge

    def put(self, uri, body=None):
        url = '%s/%s/%s/%s' % (self.bridge.base_url, self.rest_group,
                               self.id, uri)
        req = put(url, data=json.dumps(body))
        #print(req.text)
        return req

    def get(self, uri):
        url = '%s/%s' % (self.bridge.base_url, uri)
        req = get(url)
        return req
