import argparse
import pathlib

import lang
import constants


class ModCLI:
    lang_parse = lang.Lang()

    def argparster(self):
        parster = argparse.ArgumentParser()
        parster.add_argument("-add", help=self.lang_parse.translate("help.add"), type=pathlib.Path)
        parster.add_argument("-version",
                             "-ver",
                             help=self.lang_parse.translate("help.version"),
                             action="version",
                             version="{name} {ver}".format(name=constants.NAME, ver=constants.VERSION))
        args = parster.parse_args()
        print(args.add)

    def __init__(self):
        self.argparster()


if __name__ == '__main__':
    ModCLI()
