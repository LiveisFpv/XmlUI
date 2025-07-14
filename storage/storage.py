from typing import List, Tuple
from models.phrase import Phrase
from models.value import Value
from storage.quieries.phrases import PhraseQueries
from storage.quieries.values import ValueQueries

class StorageInterface:
    def searchPhrasesByText(text:str)->Tuple[List[Phrase],str]:
        """
        Поиск фраз по тексту
        
        Args:
            text: Текст для поиска
            
        Returns:
            Кортеж из:
            - Список найденных фраз
            - Сообщение об ошибке (пустая строка если ошибок нет)
        """
        raise NotImplementedError()
    
    def getPhrases()->Tuple[List[Phrase],str]:
        """
        Получение всех фраз
            
        Returns:
            Кортеж из:
            - Список найденных фраз
            - Сообщение об ошибке (пустая строка если ошибок нет)
        """
        raise NotImplementedError()

    def getValues()->Tuple[List[Phrase],str]:
        """
        Получение всех значений
            
        Returns:
            Кортеж из:
            - Список найденных значений
            - Сообщение об ошибке (пустая строка если ошибок нет)
        """
        raise NotImplementedError()

    def searchValuesByText(text:str)->Tuple[List[Value],str]:
        """
        Поиск значений по тексту
        
        Args:
            text: Текст для поиска
            
        Returns:
            Кортеж из:
            - Список найденных значений
            - Сообщение об ошибке (пустая строка если ошибок нет)
        """
        raise NotImplementedError()
    


class Storage(StorageInterface):
    def __init__(self):
        # Получаем данные из XML/JSON/DB
        self.Values=[]
        self.Phrases=[]
    
    def search_phrases_by_text(self, text: str) -> Tuple[List[Phrase], str]:
        return PhraseQueries.search_by_text(text)
    
    def search_values_by_text(self, text: str) -> Tuple[List[Value], str]:
        return ValueQueries.search_by_text(text)