import datetime

import constants


class LogLevel:
    debug = "DEBUG"
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    critical = "CRITICAL"


def log(s: str, source="", level=LogLevel.info):
    time = datetime.datetime.today().strftime("%c")
    print("[", time, "]", "(", level, ")", end="", sep="")
    if source != "":
        print("{", source, "}", end="", sep="")
    print(" " + s)


def debug(s: str, source=""):
    if constants.DEBUG:
        log(s, source, LogLevel.debug)


def info(s: str, source=""):
    log(s, source, LogLevel.info)


def warn(s: str, source=""):
    log(s, source, LogLevel.warn)


def error(s: str, source=""):
    log(s, source, LogLevel.error)


def critical(s: str, source=""):
    log(s, source, LogLevel.critical)
