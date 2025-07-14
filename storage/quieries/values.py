from typing import List, Tuple, Optional
from models.value import Value

class ValueQueries:
    """Класс для работы с запросами значений"""

    @staticmethod
    def search_by_text(text: str) -> Tuple[List[Value], str]:
        raise NotImplementedError()