from pathlib import PurePath
import json

class JsonFile:
    def __init__(self, path: PurePath, filetype="") -> None:
        if filetype == "":
            f = open(path, "r", encoding="utf-8")
            try:
                if f.read().startswith("{"):
                    filetype = "dict"
                elif f.read().startswith("["):
                    filetype = list
                else:
                    raise Exception("Unkdown json file type: " + path + ".")
            finally:
                f.close()
        self.file = open(path, "r+", encoding="utf-8")
        self.text = self.file.read()
        if filetype == "list":
            self.obj = list(json.loads(self.text))
        elif filetype == "dict":
            self.obj = dict(json.loads(self.text))
        else:
            raise Exception("Unkdown json file type: " + filetype + ".")
    
    def edit(self, new: list | dict) -> None:
        self.obj = new
        self.text = str(new)
    
    def get(self) -> dict | list:
        return self.obj

    def store(self) -> None:
        self.file.close()


class QuickAccess:
    @staticmethod
    def json_to_dict(path) -> dict:
        f = JsonFile(path, "dict")
        c = f.get()
        f.store()
        return c

    @staticmethod
    def json_to_list(path) -> list:
        f = JsonFile(path, "list")
        c = f.get()
        f.store()
        return c