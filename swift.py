from swiftclient.client import get_auth
from swiftclient import Connection, ClientException

from config import config

class SwiftUploader(object):
    def __init__(self):
        self._auth_url = config.get('swift', 'keystone_url')
        self._region_name = config.get('swift', 'region_name')
        self._tenant_name = config.get('swift', 'tenant_name')
        self._user_name = config.get('swift', 'user_name')
        self._password = config.get('swift', 'password')

        self.container_name = config.get('swift', 'container_name')
        self.url, self.token = get_auth(self._auth_url,
                                        self._user_name,
                                        self._password,
                                        tenant_name=self._tenant_name,
                                        auth_version=2,
                                        os_options={'region_name': self._region_name})
        self.uploader = Connection(preauthtoken=self.token,
                                   preauthurl=self.url)


    def initialize_container(self):
        con = self._exist_container()

        if not con:
            self._create_container()

        return self.url + '/' + self.container_name


    def _exist_container(self):
        try:
            ret = self.uploader.head_container(self.container_name)
        except:
            ret = False
        return ret

    def _create_container(self):
        self.uploader.put_container(self.container_name, headers={'x-container-read':'.r:*,.rlistings'})


    def upload_image(self, name, path):
        ret = False

        with open(path, 'ro') as f:
            ret = self.uploader.put_object(self.container_name, name, f)

        if ret:
            return self.url + '/' + self.container_name + '/' + name
        else:
            return ''

