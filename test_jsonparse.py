import jsonparse
import pytest


def test_test():
    with pytest.raises(FileNotFoundError):
        jsonparse.JsonFile("C:\\a.txt")
