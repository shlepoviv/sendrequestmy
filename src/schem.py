import json
from pathlib import Path

def get_schem(name_schem:str) -> dict:
    path_schem = Path('src','schems','.'.join([name_schem,'json']))
    with open(path_schem) as file_scheme:
        scheme = json.load(file_scheme)
    return scheme
