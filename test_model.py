import pytest
from contextlib import nullcontext as does_not_raize

from model import Contact, ContactsList
from pathlib import Path


class TestContactsList:
    @pytest.mark.parametrize(
        'path, res, expectation',
        [
            ('./data_contacts/test.json', 4,  does_not_raize()),
            ('./data_contacts/tt.json', 0, pytest.raises(FileNotFoundError)),
            ('', 0, pytest.raises(IsADirectoryError)),
        ])
    

    def test_load_from_file(self, path, res, expectation):
        with expectation:
            print(path)
            path = Path(path)
            t_model = ContactsList()
            t_model.load_from_file(path)
            assert len(t_model.contacts) == res


    @pytest.mark.parametrize(
        'path, expectation',
        [
            ('./data_contacts/save_test.json', does_not_raize()),
            ('', pytest.raises(FileNotFoundError)),
        ])

    def test_save_to_file(self, path, expectation):
        with expectation:
            contacts = ContactsList()
            add_contact = Contact(1,"Максим","Иванов","Матвеевич","+7(499)245-83-56","Костоправы","impiety embitter exposit")
            contacts.add_contact(add_contact)
            contacts.save_to_file(path)
            assert Path(path).exists()


    @pytest.mark.parametrize(
        'id_, name, last_name, surname, phone, company, comment, res',
        [
            (1,"Максим","Иванов","Матвеевич","+7(499)245-83-56","Костоправы","impiety embitter exposit", 1),
            (2,"Дмитрий","Сизов","Макарович","+7(499)439-62-77","ООО «Петрофф-Аудит»","stopgap pimple cooperate", 1),
            (3,"", "", "", "", "", "", False)
        ])
    

    def test_add_contact(self, id_, name, last_name, surname, phone, company, comment, res):
        contacts = ContactsList()
        add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
        contacts.add_contact(add_contact)
        assert len(contacts.contacts) == res


    @pytest.mark.parametrize(
        'id_, name, last_name, surname, phone, company, comment, res, expectation',
        [
            (1,"Максим","Иванов","Матвеевич","+7(499)245-83-56","Костоправы","impiety embitter exposit", 1, does_not_raize()),
            (2,"Дмитрий","Сизов","Макарович","+7(499)439-62-77","ООО «Петрофф-Аудит»","stopgap pimple cooperate", 1, pytest.raises(TypeError))

        ])
    

    def test_find_contact_by_name(self, id_, name, last_name, surname, phone, company, comment, res, expectation):
        with expectation:
            contacts = ContactsList()
            add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
            contacts.add_contact(add_contact)
            result = contacts.find_contact_by_name('Максим')
            assert len(result) == res

    @pytest.mark.parametrize(
        'id_, name, last_name, surname, phone, company, comment',
        [
            (1,"Максим","Иванов","Матвеевич","+7(499)245-83-56","Костоправы","impiety embitter exposit"),
            (2,"Дмитрий","Сизов","Макарович","+7(499)439-62-77","ООО «Петрофф-Аудит»","stopgap pimple cooperate")

        ])


    def test_update_contact(self, id_, name, last_name, surname, phone, company, comment):
        contacts = ContactsList()
        add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
        new_contact = Contact(1,'t','t','t','t','t','t')
        contacts.add_contact(add_contact)
        contacts.update_contact(0, new_contact)

        assert contacts.contacts[0].name == 't'
        



    @pytest.mark.parametrize(
        'id_, name, last_name, surname, phone, company, comment',
        [
            (1,"Максим","Иванов","Матвеевич","+7(499)245-83-56","Костоправы","impiety embitter exposit"),
            (2,"Дмитрий","Сизов","Макарович","+7(499)439-62-77","ООО «Петрофф-Аудит»","stopgap pimple cooperate")

        ])

    def test_delete_contact(self, id_, name, last_name, surname, phone, company, comment):
        contacts = ContactsList()
        add_contact = Contact(id_, name, last_name, surname, phone, company, comment)
        contacts.add_contact(add_contact)
        contacts.delete_contact(1)
        assert  contacts.contacts == []
