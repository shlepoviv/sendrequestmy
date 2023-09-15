import json
from pathlib import Path

def get_schem(name_schem:str) -> dict:
    path_schem = Path('src','schems','.'.join([name_schem,'json']))
    with open(path_schem,'r',encoding='utf-8') as file_scheme:
        scheme = json.load(file_scheme)
    return scheme
