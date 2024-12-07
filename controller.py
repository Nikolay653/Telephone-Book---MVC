"""
Класс контроллер, он управляет всей программой
"""

from dataclasses import asdict

from model import ContactsList, Contact
from view import clear, View



class Controller:
    """ 
    Класс Controller, управляет всей программой
    """
    def __init__(self):
        self.model = ContactsList()
        self.view = View()

    def run(self):
        """ 
        Главный событийный цикл 
        """
        while True:
            self.view.show_menu()
            user_choice = self.view.get_user_choice()


            if user_choice == '1':
                # Открыть файл
                if self.model.contacts and self.view.info_saved_data():
                    filename = self.view.ask_for_filename_save()
                    self.model.save_to_file(filename)
                self.model.contacts = []
                filename = self.view.ask_for_filename()
                self.model.load_from_file(filename)
                self.view.info_yes_open_file()


            elif user_choice == '2':
                # Сохранить файл
                if self.model.contacts:
                    filename = self.view.ask_for_filename_save()
                    self.model.save_to_file(filename)
                    self.view.info_saved_data()
                else:
                    self.view.warning_no_contacts()


            elif user_choice == '3':
                # Показать все контакты
                contacts = self.model.get_contacts()
                self.view.display_contacts(contacts, 30, '')


            elif user_choice == '4':
                # Создать контакт
                result = self.view.ask_for_contact()
                new_contact = Contact(len(self.model.contacts) + 1,
                                      result['name'],
                                      result['last_name'],
                                      result['surname'],
                                      result['phone'],
                                      result['company'],
                                      result['comment'])
                if self.model.add_contact(new_contact):
                    self.view.info_yes_new_contact()
                else:
                    self.view.info_no_new_contact()


            elif user_choice == '5':
                # Найти контакт
                if self.model.contacts:
                    clear()
                    self.view.title_search()
                    name = self.view.input_name_phone_searche()
                    contacts_search = self.model.find_contact_by_name(name)
                    if contacts_search:
                        self.view.display_contacts(contacts_search, 30, 'search')
                    else:
                        self.view.info_no_serch_contact()
                else:
                    self.view.info_no_open_data_file()


            elif user_choice == '6':
                # Обновление контакта
                #self.view.title_update_contact()
                id_contact = self.view.display_contacts(self.model.contacts, 20, 'update')
                if id_contact:
                    contact_update = asdict(self.model.contacts[id_contact - 1])
                    result_update_contact = self.view.update_contact_info(contact_update)
                    self.model.update_contact(id_contact - 1, Contact(result_update_contact['id'],
                                                                      result_update_contact['name'],
                                                                      result_update_contact['last_name'],
                                                                      result_update_contact['surname'],
                                                                      result_update_contact['phone'],
                                                                      result_update_contact['company'],
                                                                      result_update_contact['comment']))
                else:
                    self.view.info_error_choice()



            elif user_choice == '7':
                # Удалить контакт
                #self.view.delete_contact_info()
                del_contact_id = self.view.display_contacts(self.model.contacts, 20, 'delete')
                if del_contact_id:
                    self.model.delete_contact(del_contact_id)
                else:
                    self.view.info_warning_delete_contact()


            elif user_choice == '0':
                if self.model.contacts and self.view.info_saved_data():
                    filename = self.view.ask_for_filename_save()
                    self.model.save_to_file(filename)
                    self.view.info_yes_saved_file()
                # Выход
                break


            else:
                self.view.info_error_choice()
