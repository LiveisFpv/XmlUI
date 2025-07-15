from typing import List, Tuple
from models.phrase import Phrase
from models.value import Value
from utils.XMLparser import XMLParser

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
    
    def get_phrases()->Tuple[List[Phrase],str]:
        """
        Получение всех фраз
            
        Returns:
            Кортеж из:
            - Список найденных фраз
            - Сообщение об ошибке (пустая строка если ошибок нет)
        """
        raise NotImplementedError()

    def get_values()->Tuple[List[Value],str]:
        """
        Получение всех значений
            
        Returns:
            Кортеж из:
            - Список найденных значений
            - Сообщение об ошибке (пустая строка если ошибок нет)
        """
        raise NotImplementedError()

    def search_values_by_text(text:str)->Tuple[List[Value],str]:
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
        self.Values=[]
        self.Phrases=[]

    def load_data(self,filepath: str)-> str|None:
        phrases, values, error = XMLParser.load_from_file(filepath)
        if error:
            return error
        
        self.Phrases = phrases
        self.Values = values

        return None 
    
    def save_data(self, filepath: str) -> str|None:
        return XMLParser.save_to_file(filepath, self.Phrases, self.Values)
    
    def search_phrases_by_text(self, text: str) -> Tuple[List[Phrase], str|None]:
        return NotImplementedError()
    
    def get_phrases(self) -> Tuple[List[Phrase], str|None]:
        return self.Phrases, None
    
    def get_values(self) -> Tuple[List[Value], str|None]:
        return self.Values, None
    
    def search_values_by_text(self, text: str) -> Tuple[List[Value], str|None]:
        return NotImplementedError()