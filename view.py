"""
Класс View, выводит информацию на консоль

Методы класса:
    show_menu() - показывает меню
    get_user_choice(self) - выбор номера меню
    list_file - список файлов
    ask_for_filename(self) - выбор файла для открытия
    ask_for_filename_save(self) - возвращает путь для сохранения контактов
    ask_for_contact(self) - добавления нового контакта
"""
import os
from pathlib import Path
import itertools

from model import ContactsList



def clear():
    """ 
    Вспомогательная функция для очистки экрана
    """
    os.system('cls' if os.name == 'nt' else 'clear')


class View:

    def show_menu(self):
        """ 
        Печатает на экране меню
        """
        clear()
        print('    ' + '-' * 29)
        print('    |   Телефонный справочник   |')
        print('    ' + '-' * 29)
        print('        Меню:')
        print('    [1] Открыть файл')
        print('    [2] Сохранить файл')
        print('    [3] Показать все контакты')
        print('    [4] Добавить новый контакт')
        print('    [5] Найти контакт')
        print('    [6] Изменить контакт')
        print('    [7] Удалить контакт')
        print('    [0] Выход\n')


    def get_user_choice(self) -> str:
        """
        Выбор пункта меню

        Args:
            None
        
        Returns:
            (str): возвращает номер пункта меню
        """
        choice = input('    Введите номер пункта меню: ')
        return choice


    def list_file(self) -> list:
        """
        Показывает список файлов

        Args:
            None
        
        Returns:
            (list): возвращает список путей файлов
        """
        paths = list(map(str, Path('./data_contacts/').glob('*.json')))
        print('\n      Список файлов')
        for i, path in enumerate(paths):
            print(f'    [{i}]   {path[14:]}')
        return paths
    

    def ask_for_filename(self) -> Path:
        """
        Меню для выбора файла для открытия 

        Args:
            None
        
        Returns:
            (Path): Путь до открытия файла
        """
        clear()
        print('    ' + '-' * 31)
        print('    ' + '|      Открытие файла         |')
        print('    ' + '-' * 31)
        while True:
            result = self.list_file()
            command = input('\n    Введите номер файла : ')
            if command.isdigit() and int(command) < len(result):
                return Path(result[int(command)])
            else:
                print('    Неверный выбор. Попробуйте еще раз')


    def ask_for_filename_save(self) -> Path:
        """
        Меню для возвращения полного пути 
        Args:
            None
        
        Returns:
            (Path): Путь для сохранения файла
        """
        clear()
        print('    ' + '-' * 31)
        print('    ' + '|    Сохранение данных в файл  |')
        print('    ' + '-' * 31)
        while True:
              file_name = input('\n    Введите имя файла без расширения: ')
              if Path('./data_contacts/' + file_name + '.json').exists():
                  command = input('    Файл существует перезаписать ? < Y,Д > - перезаписать, < N, Н > - нет> , :')
                  if command in ['Y', 'y', 'Д', 'д']:
                      return Path('./data_contacts/' + file_name + '.json')
              elif file_name:
                  return Path('./data_contacts/' + file_name + '.json')
   

    def ask_for_contact(self) -> dict:
        """
        Добавление нового контакта
            
        Args:
            None
        
        Returns:
            (dict): новый словарь контакта
        """
        clear()
        print('    ' + '-' * 31)
        print('    ' + '|  Добавление нового контакта |')
        print('    ' + '-' * 31)
        last_name = input('\n    Введите Фамилию: ')
        name = input('    Введите Имя: ')
        surname = input('    Введите Отчество: ')
        phone = input('    Введите телефон контакта: ')
        company = input('    Введите название компании: ')
        comment = input('    Введите комментарии: ')
        return {'name': name,
                'last_name': last_name,
                'surname': surname,
                'phone': phone,
                'company': company,
                'comment': comment }


    @staticmethod
    def title_search():
        """ 
        Рамка поиска
        """
        clear()
        print('      ' + '-' * 31)
        print('      |            Поиск            |')
        print('      ' + '-' * 31)


    @staticmethod
    def title_update_contact():
        """ 
        Инфо об обновлении, небольшая справка
        """
        #clear()
        print('    ' + '-' * 31)
        print('    ' + '|       Обновление контакта    |')
        print('    ' + '-' * 31 + '\n')
        print('    Для обновления контакта выбирите из таблицы id контакта')
        print('    для этого нужно ввести его, для листания нажимайте Enter')
        #input('\n    Для продолжения нажмите любую клавишу... ')


    @staticmethod
    def info_yes_open_file():
        """ 
        Текстовое сообщение, незнал куда пихнуть 
        """
        print("\n    Файл успешно открыт!\n")


    @staticmethod
    def info_yes_saved_file():
        """
        Текстовое сообщение, больше негде было принтить
        """
        print("\n    Файл успешно сохранен!\n")


    @staticmethod
    def warning_no_contacts():
        """
         Текстовое сообщение 
        """
        print('\n    WARNING: Контакты пусты нечего сохранять')


    @staticmethod
    def info_yes_new_contact():
        """
        Текстовое сообщение
        """
        print("\n    Контакт успешно создан!\n")
        input('    Для продолжения нажмите любую клавишу... ')
    

    @staticmethod
    def info_no_new_contact():
        """
        Текстовое сообщение
        """
        print("\n    Контакт не добавлен, пустые поля!\n")
        input('    Для продолжения нажмите любую клавишу... ')


    @staticmethod
    def input_name_phone_searche() -> str:
        """ 
        Ввод чего мы ишем

        Returns:
            (str): возвращает строку параметра, чего, кого ищем
        """
        return input("\n   Введите имя или фамилию или телефон или компанию для поиска: ")


    @staticmethod
    def info_no_serch_contact():
        """ 
        Текстовое сообщение, незнал куда пихнуть 
        """
        print('    Нет найденных контактов')
        input('    Для продолжения нажмите любую клавишу... ')


    @staticmethod
    def info_no_open_data_file():
        """
         Текстовое сообщение
        """
        print('    Не открыта ни одна база данных')
        input('    Для продолжения нажмите любую клавишу... ')


    @staticmethod
    def info_warning_delete_contact():
        """ 
        Текстовое сообщение
        """
        print('    Возникла ошибка удаления контакта')
        input('    Для продолжения нажмите любую клавишу... ')


    @staticmethod
    def info_error_choice():
        """
        Текстовое сообщение, незнал куда пихнуть 
        """
        print("\n    Неверный выбор. Попробуйте еще раз.\n")


    @staticmethod
    def info_saved_data() -> bool:
        """ 
        Сообщает о несохраненых данных

        Returns:
            (bool): возвращает ответ
        """
        command = input('    Несохраненые данные < Y,Д > - сохранить, < N, Н > - нет> :')
        if command in ['Y', 'y', 'Д', 'д']:
            return True
        else:
            return False


    @staticmethod
    def _mod_contact(rename_param:str, name_param: str) -> str:
        """
        Вспомогательный метод для обновления контакта
            
        Args:
            rename_param (str):  что мы меняем
            name_param (str) : название параметра чего мы меняем
        
        Returns:
            (str): возвращает строку параметра
        """
        print('\n    Для изменения введите слово, если хотите оставить то клавиша [Enter]\n')
        res_modifi = input(f'    Изменить {name_param} <{rename_param}>: ')
        if res_modifi:
            return res_modifi
        else:
            return rename_param


    def update_contact_info(self, contact:dict) -> dict:
        """
        Обновление контакта
            
        Args:
            contacts (dict):  словарь контакта для изменения
        
        Returns:
            contact (dict): обновленный словарь контакта
        """
        clear()
        return {
            'id': contact['id'],
            'name': self._mod_contact(contact['name'], 'Имя'),
            'last_name': self._mod_contact(contact['last_name'], 'Фамилие'),
            'surname': self._mod_contact(contact['surname'], 'Отчество'),
            'phone': self._mod_contact(contact['phone'], 'Телефон'),
            'company':self._mod_contact(contact['company'], 'Компания'),
            'comment':self._mod_contact(contact['comment'], 'Комментарий')
        }


    @staticmethod
    def delete_contact_info():
        """ """
        print('    ' + '-' * 31)
        print('    ' + '|       Удаление контакта       |')
        print('    ' + '-' * 31 + '\n')
        print('    Для удаление контакта выбирите из таблицы id контакта')
        print('    для этого нужно ввести его, для листания нажимайте Enter')



    @staticmethod
    def _print_table(contacts: ContactsList):
        """
        Печать таблицы контактов
            
        Args:
            contacts (ContactsList): Список контактов 
        
        Returns:
            None
        """
        # максимальная ширина колонок
        max_name_last_sur = 0
        max_phone = 0
        max_company = 0
        max_comment = 0
        for item in contacts:
            len_max_name_last_sur = len(item.name) + len(item.last_name) + len(item.surname)
            len_phone = len(item.phone)
            len_company = len(item.company)
            len_comment = len(item.comment)
            max_name_last_sur = max(max_name_last_sur, len_max_name_last_sur)
            max_phone = max(max_phone, len_phone)
            max_company = max(max_company, len_company)
            max_comment = max(max_comment, len_comment)
        nls = 'ФИО'
        phon = 'Телефон'
        comp = 'Компания'
        comm = 'Комментарии'
        otstup = '   '
        print(otstup + '=' * (max_name_last_sur + max_phone + max_company + max_comment + 18))
        print(f'{otstup} id  | {nls:{max_name_last_sur + 3}} | {phon:{max_phone + 2}} | {comp:{max_company + 2}} | {comm:{max_comment}}')
        print(otstup + '=' * (max_name_last_sur + max_phone + max_company + max_comment + 18))
        for item in contacts:
            fio = item.last_name + ' ' + item.name + ' ' + item.surname
            print(f'{otstup}{item.id:4} | {fio:{max_name_last_sur + 3}} | {item.phone:{max_phone + 2}} | {item.company:{max_company + 2}} | {item.comment:{max_comment}}')
        print(otstup + '=' * (max_name_last_sur + max_phone + \
                              max_company + max_comment + 18) + '\n')


    @staticmethod
    def _count_srez(count_elements: int, step: int):
        """
        Вспомогательная функция генератор, возвращает пару чисел
        с шагом step
        Пример: step = 20, coint_elements = 30

                 0 - 20
                20 - 30
            
        Args:
            count_elements (int): указывает на общее количество строк в ContactsList
            step (int): количество строк для печати на экране

        Returns:
            None
        """
        start = 0
        for end in itertools.count(step, step=step):
            if end < count_elements:
                yield (start, end)
                start = end
            else:
                start = end - step
                end = count_elements
                yield (start, end)
                break


    def display_contacts(self, contacts: ContactsList, step: int, info:str) -> int:
        """
        Печатает таблицу с контактами

        Args:
            contacts (ContactsList): список контактов
            step (int): количество строк для печати

        Returns:
            None
        """
        if not contacts:
            print('\n    !!! Контакты отсуствуют.')
            input('    Для продолжения нажмите любую клавишу... ')

        else:
            for start, end in self._count_srez(len(contacts), step):
                clear()
                if info == 'delete':
                    self.delete_contact_info()
                elif info == 'update':
                    self.title_update_contact()
                elif info == 'search':
                    self.title_search()

                self._print_table(contacts[start: end])
                command = input('    Cледующая страница Enter: ')
                if command.isdigit() and int(command) <= len(contacts):
                    return int(command) if command else 0
