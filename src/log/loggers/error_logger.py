from src.log.loggers.base_logger import BaseLogger
import logging

class ErrorLogger(BaseLogger):
    @classmethod
    def log(cls, message: str) -> None:
        logger = cls._get_logger("error_logger", "error.log", logging.ERROR)
        logger.error(message)