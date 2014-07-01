#!/usr/bin/env python
# -*- coding:utf-8 -*-

import httplib2
import json

from config import config

class SimpleRestClient(object):
    def __init__(self):
        self._endpoint = config.get('rest-server', 'rest_endpoint')
        self._client = httplib2.Http(timeout=5)

    def get_contents(self):
        return self._get(self._endpoint)

    def post_content(self, data):
        return self._post(self._endpoint, data)

    def _get(self, url):
        resp, contents = self._client.request(url, "GET")
        return json.loads(contents)

    def _post(self, url, text):
        data = json.dumps({"text": text})
        resp, contents = self._client.request(url, "POST", data)
        return resp
    