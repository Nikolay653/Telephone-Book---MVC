""" 
Модель базы контактов состоящих из двух классов.

    Класс Contact - описание полей данных
    Класс ContactsList - список класса Contact
"""

from dataclasses import dataclass, asdict
import json
from typing import List
from pathlib import Path


@dataclass
class Contact:
    """Класс данных контактов"""
    id:int
    name: str
    last_name: str
    surname: str
    phone : str
    company: str
    comment: str

    def is_empty(self) -> bool:
        """Проверка полей на пустоту

        Returns:
            bool: _description_
        """
        if self.name or self.last_name or self.surname or self.phone or self.company:
            return False
        else:
            return True


class ContactsList:
    """ Класс список контактов """
    def __init__(self):
        self.contacts: List[Contact] = []


    def _update_id(self):
        """ Обновление id контактов"""
        for i, contact in enumerate(self.contacts, start = 1):
            contact.id = i


    def load_from_file(self, filename: Path):
        """
        Загружает из json файла контакты

        Args:
            filename (Path): Путь до файла
 
        Returns:
            None
        """
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data_load = json.load(file)
            for item in data_load['data']:
                self.contacts.append(Contact(item['id'],
                                            item['name'],
                                            item['last_name'],
                                            item['surname'],
                                            item['phone'],
                                            item['company'],
                                            item['comment']))
            self._update_id()

        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        
        except IsADirectoryError:
            raise IsADirectoryError(f"This is directory")
            


    def save_to_file(self, filename: Path):
        """
        Сохраняет контакты в файл json
        
        Args:
            filename (Path): Путь до файла
 
        Returns:
            None
        """
        self._update_id()
        data = {'data': [asdict(contact) for contact in self.contacts]}
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        
        except IsADirectoryError:
            raise IsADirectoryError(f"This is directory")


    def add_contact(self, contact: Contact) -> bool:
        """
        Добавляет новый контакт в список контактов

        Args:
            contact (Contact): класс Contact, описание данных контакта

        Returns:
            None
        """
        if contact.is_empty():
            return False
        else:
            self.contacts.append(contact)
            return True


    def find_contact_by_name(self, name: str) -> list[Contact] | None:
        """
        Поиск по контактам, ищет во всех полях

        Args:
            name (str): что мы ишем

        Returns:
            Contact [list]: возвращает список найденных контактов
        """
        result = []
        for elem in self.contacts:
            if name in (elem.name, elem.last_name, elem.surname, elem.phone, elem.company):
                result.append(elem)

        return result if result else None


    def update_contact(self, id_contact: int, new_contact: Contact):
        """
        Обновляет контакт по id

        Args:
            id_contact (int): id контакта для обновления
            new_contact (Contact): заменяем существующий контакт на обновленный по индексу

        Returns:
            None
        """
        self.contacts[id_contact] = new_contact


    def delete_contact(self, id_contact: int):
        """
        Удаляет контакт по id

        Args:
            id_contact (int): id контакта для удаления

        Returns:
            None
        """
        if id_contact <= len(self.contacts):
            del self.contacts[id_contact - 1]
            self._update_id()


    def get_contacts(self) -> List[Contact]:
        """
        Возвращает список контактов

        Args:
            None

        Returns:
            Contact (List): список контактов
        """
        return self.contacts
