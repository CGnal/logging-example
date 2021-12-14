from slack import WebClient

class SlackHandler(StreamHandler):
    def __init__(self, config):
        StreamHandler.__init__(self)
        self.token = config.slack.token
        self.proxy = config.proxies.http
        self.channel = config.slack.channel
        self.prefix =  config.slack.prefix
        self.slack_client = WebClient(token=self.token, run_async=False, proxy=self.proxy)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - [%(name)s] - [%(module)s] - %(funcName)s() - %(message)s"
        )
        self.setFormatter(formatter)

    def emit(self, record):
        if self.prefix is not None:
            msg = f"{self.prefix} {self.format(record)}"
            self.slack_client.chat_postMessage(channel=self.channel, text=msg)