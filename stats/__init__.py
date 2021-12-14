from cgnal.logging import WithLogging

class Mean(WithLogging):

    def __init__(self):
        self.logger.info("Initializing")
        pass

    def compute(self, values):
        self.logger.debug(f"Dimension of values: {len(values)}")
        return sum(values)/len(values)