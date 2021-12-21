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

    logger.info("This is the main...")

    process_logger.debug("This is a logger process")

    logger.debug("Instantiating the process")

    proc = Process(10)

    logger.error("This is an error")

    warnings.warn("This is a warning", FutureWarning)

    logger.warning("This is a warning of the runner")

    logger.debug("Execution now...")

    res = proc.run()

    logger.info(f"Result of the process {res}")
