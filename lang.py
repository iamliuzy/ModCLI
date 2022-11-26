import jsonparse
import locale


class Lang:
    def __init__(self):
        lang = locale.getdefaultlocale()[0]
        try:
            json = jsonparse.QuickAccess.json_to_dict(".\\assets\\lang\\{lang}.json".format(lang=lang))
        except FileNotFoundError:
            json = jsonparse.QuickAccess.json_to_dict(".\\assets\\lang\\en_us.json")
        self._lang_translate = json

    def translate(self, keyword: str):
        try:
            return self._lang_translate[keyword]
        except KeyError:
            import logging
            logging.warning("No such keyword " + keyword + ".")
            return keyword
