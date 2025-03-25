import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)
    file_handler = RotatingFileHandler("app.log", maxBytes=5*1024*1024, backupCount=3)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
logger = setup_logger()