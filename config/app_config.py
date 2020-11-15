from animal.settings import DEBUG
from config import DevConfig, ProdConfig


class AppConfig():
    def __init__(self):
        if DEBUG == True:
            DevConfig.__init__(self)
        else:
            ProdConfig.__init__(self)