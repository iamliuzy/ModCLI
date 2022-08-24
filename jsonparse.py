from pathlib import Path
from pykson import Pykson

def _open(path:Path):
    path = path.resolve()
    file = open(path, "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content

def _write(path:Path, content:str):
    path = path.resolve()
    file = open(path, "w", encoding="utf-8")
    file.write(content)
    file.close()

def json_to_object(json:str, pojo):
    return Pykson.from_json(json, pojo)

def file_to_object(json:Path, pojo):
    return json_to_object(_open(json), pojo)

def object_to_json(pojo):
    return Pykson.to_json(pojo)

def object_to_file(json:Path, pojo):
    _write(json, object_to_json(pojo))

def json_to_dict(json:str):
    return json_to_object(json, dict)

def file_to_dict(json:Path):
    return file_to_object(json, dict)

def json_to_list(json:str):
    return json_to_object(json, list)

def file_to_list(json:Path):
    return file_to_object(json, list)