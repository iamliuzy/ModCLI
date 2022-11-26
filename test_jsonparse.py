from jsonparse import *
import pytest

def test_test():
    with pytest.raises(FileNotFoundError):
        JsonFile("C:\\a.txt")