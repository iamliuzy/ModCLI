import json
import pathlib
import logging


class Json:
    """
    Json API for this program.
    """

    def __init__(self, is_list=False, path=pathlib.PurePath(".\\config.json")):
        """
        is_list: If this json file is a list, it should be "True".
        path: The path of the json file.
        """
        self.is_List = is_list

        self.path = path

        if not pathlib.Path(str(self.path)).exists():
            logging.warning("No such json file '" + str(self.path) + ".")
            raise FileNotFoundError("No such json file '" + str(self.path) + "'.")

        logging.info("Loading json file '" + str(path) + "'.")
        self.file = open(str(self.path), "r", encoding="utf-8")
        self.pure_content = self.file.read()
        logging.info("Load successful.")
        if self.is_List:
            self.content = list(json.loads(self.pure_content))
        else:
            self.content = dict(json.loads(self.pure_content))
        self.file.close()

    def parse(self) -> list | dict:
        self.file.close()
        return self.content

    def merge(self, content):
        self.content = content
        self.save()
        return True

    def save(self):
        self.file = open(str(self.path), "w")
        self.file.write(str(self.content))
        self.file.close()
