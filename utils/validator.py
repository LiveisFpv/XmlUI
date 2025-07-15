class Validator:
    class ValueValidator:
        @staticmethod
        def is_valid_key(key: str) -> bool:
            """Проверяет, что ключ не пустой и не содержит недопустимых символов."""
            if not key or not key.strip():
                return False
            if any(char in key for char in ['&', "[", "]"]):
                return False
            return True

        @staticmethod
        def is_valid_text(text: str) -> bool:
            """Проверяет, что текст не пустой. и не содержит недопустимых символов."""
            if not text or not text.strip():
                return False
            if any(char in text for char in ['<', '>', '&', '"', "'", "{", "}", "[", "]"]):
                return False
            return True
    
    class PhraseValidator:
        @staticmethod
        def is_valid_key(key: str) -> bool:
            """Проверяет, что ключ не пустой и не содержит недопустимых символов."""
            if not key or not key.strip():
                return False
            if any(char in key for char in ['&', "[", "]"]):
                return False
            return True

        @staticmethod
        def is_valid_text(text: str) -> bool:
            """Проверяет, что текст не пустой, не содержит недопустимых символов и {} не вложены друг в друга."""
            if not text or not text.strip():
                return False
            if any(char in text for char in ["[", "]"]):
                return False
            depth = 0
            for char in text:
                if char == "{":
                    depth += 1
                    if depth > 1:
                        return False
                elif char == "}":
                    if depth == 0:
                        return False
                    depth -= 1
            if depth != 0:
                return False
            return True