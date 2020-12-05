import logging


def test_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler("logfile.log")
    # file name where logs has to be printed

    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    # in which format it has to print

    fileHandler.setFormatter(formatter)
    # giving connectivity to logger and file handler and formatter

    logger.addHandler(fileHandler)
    logger.setLevel(logging.CRITICAL)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical issue")



