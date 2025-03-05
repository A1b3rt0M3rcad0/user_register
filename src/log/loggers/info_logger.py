from src.log.loggers.base_logger import BaseLogger
import logging

class InfoLogger(BaseLogger):
    @classmethod
    def log(cls, message: str) -> None:
        logger = cls._get_logger("info_logger", "info.log", logging.INFO)
        logger.info(message)