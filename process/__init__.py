import numpy as np  # type: ignore

from cgnal.logging import WithLogging, getLogger
from stats import Mean

logger = getLogger(__name__)

logger.info("Initialization of the Process module")


class Process(WithLogging):

    def __init__(self, n):
        self.logger.info(f"Inizializing Process with n={n}")
        self.n = n

        self.operation = Mean()

    def run(self):
        self.logger.info("Running process")

        self.logger.debug("Creating random values")

        values = np.random.random(self.n)

        self.logger.debug("First computation")

        mean1 = self.operation.compute(values)

        self.logger.info(f"Result of first operation: {mean1}")

        values = np.random.random(self.n)

        self.logger.debug("Second computation")

        mean2 = self.operation.compute(values)

        self.logger.info(f"Result of second operation: {mean2}")

        return self.operation.compute([mean1, mean2])
