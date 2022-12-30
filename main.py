import argparse
import pathlib

import lang
import constants
import mods


class ModCLI:
    lang_parse = lang.Lang()

    def arg_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-add", help=self.lang_parse.translate("help.add"), type=pathlib.Path)
        parser.add_argument("--version", "-v",
                            help=self.lang_parse.translate("help.version"), action="version",
                            version="{name} {ver}".format(name=constants.NAME, ver=constants.VERSION))
        self.args = vars(parser.parse_args())

    def __init__(self):
        self.arg_parser()
        if not self.args["add"] is None:
            mods.Mod(self.args["add"])


ModCLI()
