from pathlib import PurePath
import json

class JsonFile:
    def __init__(self, path: PurePath, filetype: str) -> None:
        self.file = open(path, "r+", encoding="utf-8")
        self.text = self.file.read()
        if filetype == "list":
            self.obj = list(json.loads(self.text))
        elif filetype == "dict":
            self.obj = dict(json.loads(self.text))
        else:
            raise Exception("Unkdown json file type: " + filetype + ".")

    def __init__(self, path: PurePath) -> None:
        file = open(path, "r", encoding="utf-8")
        try:
            if file.read().startswith("{"):
                self.__init__(path, "dict")
            elif file.read().startswith("["):
                self.__init__(path, "list")
            else:
                raise Exception("Unkdown json file type: " + path + ".")
        finally:
            file.close()

    
    def edit(self, new: list | dict) -> None:
        self.obj = new
        self.text = str(new)
    
    def get(self) -> dict | list:
        return self.obj

    def store(self) -> None:
        self.file.close()


class QuickAccess:
    @classmethod
    def json_to_dict(path) -> dict:
        f = JsonFile(path)
        c = f.get()
        f.store()
        return c

    @classmethod
    def json_to_list(path) -> list:
        f = JsonFile(path)
        c = f.get()
        f.store()
        return c