import logging
import os


class Logger:

    @staticmethod
    def get_logger():

        if not os.path.exists("logs"):
            os.makedirs("logs")

        logger = logging.getLogger("SauceDemo")

        logger.setLevel(logging.INFO)

        if not logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            file_handler = logging.FileHandler("logs/test.log")
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger