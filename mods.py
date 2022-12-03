import pathlib
import jsonparse
import zipfile
import tempfile
import toml


class Mod:
    def __init__(self, path: pathlib.Path):
        self.path = pathlib.Path(path).resolve()
        self.file = zipfile.ZipFile(self.path, mode="r")
        with tempfile.TemporaryDirectory() as tempdir:
            try:
                extracted = self.file.extract("META-INF/mods.toml", tempdir)
                self.metadata = toml.load(extracted)
                self.loader = 1
            except KeyError:
                try:
                    extracted = self.file.extract("mcmod.info", tempdir)
                    self.metadata = jsonparse.QuickAccess.json_to_list(extracted)
                    self.loader = 0
                except KeyError:
                    extracted = self.file.extract("fabric.mod.json", tempdir)
                    self.metadata = jsonparse.QuickAccess.json_to_dict(extracted)
                    self.loader = 3
        if self.loader == 1:
            print(self.metadata)
            self.name = str(self.metadata["mods"][0]["displayName"])
            self.id = str(self.metadata["mods"][0]["modId"])
            self.dependencies = list(self.metadata["dependencies"][self.id])
            self.version = str(self.metadata["mods"][0]["version"])
            self.url = str(self.metadata["mods"][0]["displayURL"])
            self.issue_url = str(self.metadata["issueTrackerURL"])
            self.description = str(self.metadata["mods"][0]["description"])
            for i in dir(self):
                if i[0] != "_":
                    print(getattr(self, i))
