import pathlib
import jsonparse
import zipfile
import tempfile
import toml


class Mod:
    name:str
    id: str
    loader: int
    path: pathlib.Path
    version: str
    update_url: str
    website_id: dict

    def __init__(self, path:pathlib.Path):
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
                    self.metadata = jsonparse.file_to_list(extracted)
                    self.loader = 0
                except KeyError:
                    extracted = self.file.extract("fabric.mod.json", tempdir)
                    self.metadata = jsonparse.file_to_dict(extracted)
                    self.loader = 3
            print(self.loader)
            print(self.metadata)

if __name__ == "__main__":
    Mod("E:\\my\\.minecraft\\.mods.shaders.respacks\\mods\\1.7\\NGTLib1.7.10.32_Forge10.13.4.1558.jar")