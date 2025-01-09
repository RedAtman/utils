import json
import logging
import platform
import sys
import time
import traceback


class JSONFormatter(logging.Formatter):
    """A formatter for the standard logging module that converts a LogRecord into JSON

    Output matches JSONLayout from https://github.com/kdgregory/log4j-aws-appenders. Any
    keyword arguments supplied to the constructor are output in a "tags" sub-object.
    """

    def __init__(self, **tags):
        self.tags = tags

    def format(self, record):
        result = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(record.created))
            + (".%03dZ" % (1000 * (record.created % 1))),
            "level": record.levelname,
            "logger": record.name,
            "message": record.msg % record.args,
            # "_message": json.loads(record.msg),
            # "_message": {"message": "{}".format(record.msg), "args": record.args},
            "hostname": platform.node(),
            "processId": record.process,
            "thread": record.threadName,
            "locationInfo": {"fileName": record.filename, "lineNumber": record.lineno},
        }

        if self.tags:
            result["tags"] = self.tags

        if record.exc_info:
            result["exception"] = traceback.format_exception(record.exc_info[0], record.exc_info[1], record.exc_info[2])

        return json.dumps(result)


def configure_logging():
    handler = logging.StreamHandler(sys.stderr)
    formatter = JSONFormatter(application="example")
    handler.setFormatter(formatter)
    logging.basicConfig(level=logging.DEBUG, handlers=[handler])


if __name__ == "__main__":
    configure_logging()
    logger = logging.getLogger(__name__)
    logger.info("Started")
    logger.debug("this is a test of %s %s", "value", "substitutions")
    try:
        raise Exception("example")
    except Exception as ex:
        logger.exception("caught exception")
    logger.info("Finished")
    # logger.info(logger.__dict__)
