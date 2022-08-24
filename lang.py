import jsonparse
import locale


class Lang:
    def __init__(self):
        lang = locale.getdefaultlocale()[0]
        try:
            json = jsonparse.Json(path=".\\assets\\lang\\" + lang + ".json").parse()
        except FileNotFoundError:
            json = jsonparse.Json(path=".\\assets\\lang\\default.json").parse()
        self.lang_translate = json

    def translate(self, keyword: str):
        try:
            return self.lang_translate[keyword]
        except KeyError:
            import logging
            logging.warning("No such keyword " + keyword + ".")
            return keyword
