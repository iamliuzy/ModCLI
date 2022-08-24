import argparse

import lang


class CMOD:
    lang_parse = lang.Lang()
    def argparster(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--add", "-a", help=self.lang_parse.translate("help.add"))
        args = parser.parse_args()
        print(args.echo)

    def __init__(self):
        self.argparster()


if __name__ == '__main__':
    CMOD()
