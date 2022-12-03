import argparse
import pathlib

import lang
import constants
import mods


class ModCLI:
    lang_parse = lang.Lang()

    def argparster(self):
        parster = argparse.ArgumentParser()
        parster.add_argument("-add", help=self.lang_parse.translate("help.add"), type=pathlib.Path)
        parster.add_argument("--version", "-v",
                             help=self.lang_parse.translate("help.version"), action="version",
                             version="{name} {ver}".format(name=constants.NAME, ver=constants.VERSION))
        self.args = vars(parster.parse_args())

    def __init__(self):
        self.argparster()
        if not self.args["add"] is None:
            mods.Mod(self.args["add"])


if __name__ == '__main__':
    ModCLI()
