import os
import logging


class DevConfig:
    def __init__(self):
        self._cur_set = 'dev'

        # logging config
        self._logging_level = logging.DEBUG
        self._logging_file_path = "/app/logs/animal_api.log"