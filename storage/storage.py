from typing import List, Tuple
from models.phrase import Phrase
from models.value import Value
from utils.XMLparser import XMLParser

class StorageInterface:
    def searchPhrasesByText(text:str)->Tuple[list[Phrase],str|None]:
        """
        Поиск фраз по тексту
        
        Args:
            text: Текст для поиска
            
        Returns:
            Кортеж из:
            - Список найденных фраз
            - Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def get_phrases()->Tuple[list[Phrase],str|None]:
        """
        Получение всех фраз
            
        Returns:
            Кортеж из:
            - Список найденных фраз
            - Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def get_phrase_by_key(key:str)->Tuple[Phrase|None, str|None]:
        """
        Получение фразы по ключу
        
        Args:
            key: Ключ фразы
            
        Returns:
            Кортеж из:
            - Фраза (None если не найдена)
            - Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def add_phrase(phrase:Phrase)->str|None:
        """
        Добавление фразы в хранилище
        
        Args:
            phrase: Фраза для добавления
            
        Returns:
            Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def edit_phrase(old_key:str, new_phrase:Phrase)->str|None:
        """
        Редактирование фразы в хранилище
        
        Args:
            old_key: Ключ старой фразы
            new_phrase: Новая фраза
            
        Returns:
            Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def delete_phrase(key:str)->str|None:
        """
        Удаление фразы из хранилища
        
        Args:
            key: Ключ фразы для удаления
            
        Returns:
            Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()

    def get_values()->Tuple[list[Value],str|None]:
        """
        Получение всех значений
            
        Returns:
            Кортеж из:
            - Список найденных значений
            - Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()

    def get_value_by_key(key:str)->Tuple[Value|None, str|None]:
        """
        Получение значения по ключу
        
        Args:
            key: Ключ значения
            
        Returns:
            Кортеж из:
            - Значение (None если не найдено)
            - Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()

    def search_values_by_text(text:str)->Tuple[list[Value],str|None]:
        """
        Поиск значений по тексту
        
        Args:
            text: Текст для поиска
            
        Returns:
            Кортеж из:
            - Список найденных значений
            - Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def add_value(value:Value)->str|None:
        """
        Добавление значения в хранилище
        
        Args:
            value: Значение для добавления
            
        Returns:
            Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()

    def edit_value(old_key:str, new_value:Value)->str|None:
        """
        Редактирование значения в хранилище
        
        Args:
            old_key: Ключ старого значения
            new_value: Новое значение
            
        Returns:
            Сообщение об ошибке (None если ошибок нет)
        """
        raise NotImplementedError()
    
    def delete_value(key:str)->str|None:
        """
        Удаление значения из хранилища
        
        Args:
            key: Ключ значения для удаления
            
        Returns:
            Сообщение об ошибке (None если ошибок нет)
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
    
    def search_phrases_by_text(self, text: str) -> Tuple[list[Phrase], str|None]:
        found_phrases = [phrase for phrase in self.Phrases if (text.lower() in phrase.text.lower() or text.lower() in phrase.key.lower())]
        return found_phrases, None
    
    def get_phrases(self) -> Tuple[list[Phrase], str|None]:
        return self.Phrases, None
    
    def get_phrase_by_key(self, key: str) -> Tuple[Phrase|None, str|None]:
        for phrase in self.Phrases:
            if phrase.key == key:
                return phrase, None
        return None, f"Фраза с ключом '{key}' не найдена"
    
    def add_phrase(self, phrase: Phrase) -> str|None:
        self.Phrases.append(phrase)
        return None
    
    def edit_phrase(self, old_key: str, new_phrase: Phrase) -> str|None:
        # Проверка, что новый ключ не совпадает с другим ключом (кроме old_key)
        for phrase in self.Phrases:
            if phrase.key == new_phrase.key and phrase.key != old_key:
                return f"Фраза с ключом '{new_phrase.key}' уже существует"
        for i, phrase in enumerate(self.Phrases):
            if phrase.key == old_key:
                self.Phrases[i] = new_phrase
                return None
        return f"Фраза с ключом '{old_key}' не найдена"
    
    def delete_phrase(self, key: str) -> str|None:
        for i, phrase in enumerate(self.Phrases):
            if phrase.key == key:
                del self.Phrases[i]
                return None
        return f"Фраза с ключом '{key}' не найдена"
    
    def get_values(self) -> Tuple[list[Value], str|None]:
        return self.Values, None
    
    def get_value_by_key(self, key: str) -> Tuple[Value|None, str|None]:
        for value in self.Values:
            if value.key == key:
                return value, None
        return None, f"Значение с ключом '{key}' не найдено"
    
    def search_values_by_text(self, text: str) -> Tuple[list[Value], str|None]:
        found_values = [value for value in self.Values if (text.lower() in value.text.lower() or text.lower() in value.key.lower())]
        return found_values, None
    
    def add_value(self, value: Value) -> str|None:
        self.Values.append(value)
        return None
    
    def edit_value(self, old_key: str, new_value: Value) -> str|None:
        # Проверка, что новый ключ не совпадает с другим ключом (кроме old_key)
        for value in self.Values:
            if value.key == new_value.key and value.key != old_key:
                return f"Значение с ключом '{new_value.key}' уже существует"
        for i, value in enumerate(self.Values):
            if value.key == old_key:
                self.Values[i] = new_value
                return None
        return f"Значение с ключом '{old_key}' не найдено"
    
    def delete_value(self, key: str) -> str|None:
        for i, value in enumerate(self.Values):
            if value.key == key:
                del self.Values[i]
                return None
        return f"Значение с ключом '{key}' не найдено"
    
    