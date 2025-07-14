from typing import List, Tuple
from models.phrase import Phrase

class PhraseQueries:
    """Класс для работы с запросами фраз"""
    
    @staticmethod
    def search_by_text(text: str) -> Tuple[List[Phrase], str]:
        raise NotImplementedError()
    