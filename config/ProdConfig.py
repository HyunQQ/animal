import os
import logging


class ProdConfig:
    def __init__(self):
        self._cur_set = 'prod'

        # logging config
        self._logging_level = logging.INFO
        self._logging_file_path = os.path.join('app', 'logs', 'animal_api.log')