import xml.etree.ElementTree as ET
from models.phrase import Phrase
from models.value import Value
from models.param import Param
from typing import List, Tuple, Optional


class XMLParser:
    @staticmethod
    def load_from_file(filepath: str) -> Tuple[List[Phrase]|None, List[Value]|None, str|None]:
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            encoding = tree.docinfo.encoding if hasattr(tree, 'docinfo') else 'utf-8'

            # Load Values
            values = []
            values_element = root.find('Values')
            if values_element is not None:
                for val in values_element.findall('Value'):
                    key = val.attrib.get('key')
                    text = val.text or ''
                    values.append(Value(key, text.strip()))

            # Load Phrases
            phrases = []
            phrases_element = root.find('Phrases')
            if phrases_element is not None:
                for phrase_elem in phrases_element.findall('Phrase'):
                    key = phrase_elem.attrib.get('key')
                    text = (phrase_elem.text or '').strip()
                    params = []

                    params_elem = phrase_elem.find('Params')
                    if params_elem is not None:
                        for param_elem in params_elem.findall('Param'):
                            name = param_elem.text.strip() if param_elem.text else ''
                            required = param_elem.attrib.get('required', 'false')
                            params.append(Param(name=name, required=required))

                    phrases.append(Phrase(key=key, text=text, params=params))

            return phrases, values, None

        except Exception as e:
            return None, None, f"Ошибка при загрузке XML: {str(e)}"

    @staticmethod
    def save_to_file(filepath: str, phrases: List[Phrase], values: List[Value]) -> str|None:
        # Создаем резервную копию файла, если он существует
        import os
        if os.path.exists(filepath):
            backup_filepath = filepath + '.bak'
            os.rename(filepath, backup_filepath)
        try:
            # Собираеи XML структуру
            root = ET.Element('Config')

            # Values
            values_el = ET.SubElement(root, 'Values')
            for val in values:
                val_el = ET.SubElement(values_el, 'Value', {'key': val.key})
                val_el.text = val.text

            values_dict = {val.key: val for val in values}
            
            def is_value(key: str) -> bool:
                return key in values_dict
            
            # Phrases
            phrases_el = ET.SubElement(root, 'Phrases')
            for phrase in phrases:
                phrase_el = ET.SubElement(phrases_el, 'Phrase', {'key': phrase.key})
                phrase_el.text = phrase.text
                if phrase.params:
                    params_el = ET.SubElement(phrase_el, 'Params')
                    for param in phrase.params:
                        # Check if the parameter is defined in values
                        param_el = ET.SubElement(params_el, 'Param', {'required': "true" if is_value(param.name) else "false"})
                        param_el.text = param.name

            # Write to file
            tree = ET.ElementTree(root)
            ET.indent(tree, space="  ", level=0)
            tree.write(filepath, encoding="utf-8", xml_declaration=True)

            return None
        except Exception as e:
            # Записываем резервную копию в случае ошибки
            if os.path.exists(backup_filepath):
                os.rename(backup_filepath, filepath)
            
            return f"Ошибка при сохранении XML: {str(e)}"
