import configparser
from pytfsclient.tfs_client_factory import TfsClientFactory


TFS_CONFIG_FILE = 'configs/tfsconfig.ini'
TFS_CONFIG_NAME = 'DEFAULT'


class TfsConfig:
    _config = configparser.ConfigParser()

    def __init__(self, config_file: str, config_name: str):
        self._config.read(config_file)
        self._settings = self._config[config_name]
        self.server = self._settings['Server']
        self.project = self._settings['Project']
        self.username = self._settings['Username']
        self.password = self._settings['Password']


class TfsClient:
    def __init__(self):
        self._config = TfsConfig(TFS_CONFIG_FILE, TFS_CONFIG_NAME)
        self._base_client = TfsClientFactory.create(self._config.server, self._config.project)
        self._base_client.authentificate_with_password(self._config.username, self._config.password)
        self.wi_client = TfsClientFactory.get_workitem_client(self._base_client)
        self.project_client = TfsClientFactory.get_project_client(self._base_client)


tfsclient = TfsClient()
