from animal.settings import DEBUG
from config.DevConfig import DevConfig
from config.ProdConfig import ProdConfig

class AppConfig(DevConfig, ProdConfig):
# class AppConfig():
    def __init__(self):
        if DEBUG == True:
            DevConfig.__init__(self)
            # pass
        else:
            ProdConfig.__init__(self)
            # pass

    @property
    def logging_level(self):
        return self._logging_level

    @property
    def logging_file_path(self):
        return self._logging_file_path

