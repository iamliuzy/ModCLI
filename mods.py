import pathlib
import jsonparse
import zipfile
import tempfile
import toml
import log
import constants


class Mod:
    """
    Object for a Minecraft Mod.
    About attribute "loader":
    | Loader     | No. |
    |------------|-----|
    | Forge(old) | 0   |
    | Forge(new) | 1   |
    | Fabric     | 2   |

    :param path: File path of mod file.
    """

    def __init__(self, path: pathlib.Path):
        self.path = pathlib.Path(path).resolve()
        self.file = zipfile.ZipFile(self.path, mode="r")
        with tempfile.TemporaryDirectory() as tempdir:
            try:
                extracted = self.file.extract("META-INF/mods.toml", tempdir)
                self.metadata = toml.load(extracted)
                self.loader = 1  # Forge new loader
            except KeyError:
                try:
                    extracted = self.file.extract("mcmod.info", tempdir)
                    self.metadata = jsonparse.QuickAccess.json_to_list(extracted)
                    self.loader = 0  # Forge old loader
                except KeyError:
                    extracted = self.file.extract("fabric.mod.json", tempdir)
                    self.metadata = jsonparse.QuickAccess.json_to_dict(extracted)
                    self.loader = 2  # Fabric loader
        if self.loader == 1:
            try:
                self.name = str(self.metadata["mods"][0]["displayName"])
                self.id = str(self.metadata["mods"][0]["modId"])
                self.dependencies = list(self.metadata["dependencies"][self.id])
                self.version = str(self.metadata["mods"][0]["version"])
                self.url = str(self.metadata["mods"][0]["displayURL"])
                self.issue_url = str(self.metadata["issueTrackerURL"])
                self.description = str(self.metadata["mods"][0]["description"])
            except KeyError as e:
                log.warn(str(e) + ' key does not exist in the manifest file of mod "' + str(self.path) + '".')
            log.debug(str(constants.DEBUG))
            for i in dir(self):
                if i[0] != "_":
                    log.debug(i + "::" + str(getattr(self, i)))
