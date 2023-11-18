from typing import Union
import os
import json

def load_json(path):
    """Load a JSON file from the given path."""
    with open(path, 'r') as f:
        return json.load(f)
    
# Desc: Loads dicts from JSON files
_dicts = [d[:-5] for d in os.listdir(os.path.abspath(os.path.dirname(__file__))) if d.endswith('.json') and d != '__init__.py']


def load_dict(name):
    if name in _dicts:
        return load_json(f'{os.path.join(os.path.dirname(__file__), name)}.json')
    else:
        raise ValueError(f'No such dict: {name}')
    
def load_all_dicts():
    return {d: load_dict(d) for d in _dicts}

# Desc: Loads lists from text files
_lists = [d[:-9] for d in os.listdir(os.path.dirname(__file__)) if d.endswith('_list.txt') and d != '__init__.py']

def load_list(name):
    if name not in _lists:
        raise ValueError(f'No such list: {name}')
    with open(f'{os.path.join(os.path.dirname(__file__), name)}_list.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]
    

class QuietDict:
    def __init__(self):
        self.items = {}

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key: Union[str, int]):
        if isinstance(key, str):
            return self.items[key]
        elif isinstance(key, int):
            return list(self.items.values())[key]
        else:
            raise TypeError("Key must be of type str or int")

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, key):
        return key in self.items

    def __repr__(self):
        return f"{self.__class__.__name__}({len(self.items)} items)"

    def __sub__(self, other):
        if isinstance(other, QuietDict):
            for key, value in self.items.copy().items():
                if key in other:
                    del self[key]

    def update(self, other=None, **kwargs):
        if other:
            if hasattr(other, "keys"):
                for key in other.keys():
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def values(self):
        return list(self.items.values())