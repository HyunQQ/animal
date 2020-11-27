import logging
import os
from django.apps import AppConfig
from logging import handlers


class AppConfig(AppConfig):
    name = 'app'

    def ready(self):
        from config import app_config
        self.app_config = app_config.AppConfig()
        self.set_logging()

    def set_logging(self):
        logger = logging.getLogger()
        console_handler = logging.StreamHandler()
        log_file_nm = os.path.join(os.getcwd(), 'log', 'animal.log')
        file_handler = handlers.TimedRotatingFileHandler(filename=log_file_nm,
                                                         when="midnight",
                                                         backupCount=4,
                                                         encoding='utf-8')

        formatter = logging.Formatter(
            fmt     = "[%(levelname)s, %(asctime)s][%(filename)s:%(lineno)s - %(funcName)s] %(message)s",
            datefmt = '%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.setLevel(self.app_config.logging_level)

