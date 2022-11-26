from mods import *
import pytest

def test_test():
    obj = Mod(".\\test_resources\\NGTLib1.7.10.32_Forge10.13.4.1558.jar")
    assert obj.loader == 0
    assert obj.metadata == [{'modid': 'NGTLib', 'name': 'NGTLib', 'description': '', 'version': '1.7.10.32', 'mcversion': '1.7.10', 'url': 'https://www.curseforge.com/members/ngt5479/projects', 'updateUrl': 'https://dl.dropboxusercontent.com/s/4dxg83j6rocd0ls/version.txt', 'authorList': ['ngt5479'], 'credits': 'Shin504, IgorKhydyakov', 'requiredMods': ['Forge'], 'parent': '', 'dependencies': []}]