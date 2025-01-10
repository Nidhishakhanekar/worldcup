import logging


class LogGenerator:

    @staticmethod
    def logData():
        logger = logging.getLogger()
        logpath = logging.FileHandler(
            "C:\\Users\\pradi\\OneDrive\\Desktop\\python new file\\HeroWorldcup\\log\\log.log")
        Format = logging.Formatter("%(asctime)s:%(funcName)s:%(message)s")
        logpath.setFormatter(Format)
        logger.addHandler(logpath)
        logger.setLevel(logging.INFO)
        return logger
