from src.domain.log.i_logger import ILogger
import logging
import os

class BaseLogger(ILogger):
    
    _loggers = {}

    @classmethod
    def _get_logger(cls, name: str, log_file: str, level: int):
        
        if name not in cls._loggers:
            logger = logging.getLogger(name)
            logger.setLevel(level)

            log_dir = "src/log/logs"
            os.makedirs(log_dir, exist_ok=True)

            file_handler = logging.FileHandler(os.path.join(log_dir, log_file))
            file_handler.setLevel(level)

            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

            logger.propagate = False

            cls._loggers[name] = logger

        return cls._loggers[name]