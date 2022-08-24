import jsonparse
import locale


class Lang:
    def __init__(self):
        lang = locale.getdefaultlocale()[0]
        try:
            json = jsonparse.file_to_dict(".\\assets\\lang\\{lang}.json".format(lang=lang))
        except FileNotFoundError:
            json = jsonparse.file_to_dict(".\\assets\\lang\\en_us.json")
        self.lang_translate = json

    def translate(self, keyword: str):
        self.__init__()
        try:
            return self.lang_translate[keyword]
        except KeyError:
            import logging
            logging.warning("No such keyword " + keyword + ".")
            return keyword
