from models.param import Param

class Phrase:
    def __init__(self, key: str, text: str, params: list[Param] = None):
        self.key = key
        self.text = text.strip()
        self.params = params if params is not None else []
