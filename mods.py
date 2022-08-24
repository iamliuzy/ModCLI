import pathlib
import jsonparse


class Mod:
    name:str
    id: str
    version: str
    update_url: str
    website_id: dict


class ModAPI:
    def add_mod(path: pathlib.Path):
        