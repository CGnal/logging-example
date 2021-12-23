from cgnal.logging import configFromFile, getLogger

configFromFile("logging.yaml")

from process import Process, logger as process_logger  # noqa: E402
import warnings  # noqa: E402
import logging  # noqa: E402

logging.captureWarnings(True)


def handle_exception(logger):
    import sys

    def wrapper(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        logger.error(
            f"{exc_type.__name__}: {exc_value}",
            exc_info=(exc_type, exc_value, exc_traceback)
        )

    sys.excepthook = wrapper

    return logger


if __name__ == "__main__":
    logger = handle_exception(getLogger("runner"))

    process_logger.info("here!!!!!")

    logger.info("This is the main...")

    logger.debug("Instantiating the process")

    proc = Process(10)

    logger.error("This is an error")

    warnings.warn("mario", FutureWarning)

    logger.warning("This is a warning")

    logger.debug("Execution now...")

    res = proc.run()

    logger.info(f"Result of the process {res}")
