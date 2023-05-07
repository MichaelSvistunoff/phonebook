from ProjectStructure.Core.Infrastructure.PhoneBook import PhoneBook


class App():

    def __init__(self):
        self.contacts = PhoneBook()
        self.menu_dict = {
            "Показать все контакты": self.contacts.show_all_contacts(),
            "Найти контакт по имени": self.contacts.search_by_name(),
            # "Найти контакт по номеру": search_by_phone,
            "Добавить новый контакт": self.contacts.add_contact(),
            # "Удалить контакт": delete,
            # "Изменить номер телефона": edit_number,
            # "Завершить программу": exit_,
        }
        self.menuList = [
            "Показать все контакты",
            "Найти контакт по имени",
            # "Найти контакт по номеру",
            "Добавить новый контакт",
            # "Удалить контакт",
            # "Изменить номер телефона",
            # "Завершить программу",
        ]

    def menu(self):
        print('Phone book:\n')
        for index, option in enumerate(self.menuList):
            print(f"{index + 1} - {option}")
        input_ = input('Выбрать действие(введите индекс): ')
        print('\n')
        while input_ not in ('1', '2', '3', '4', '5', '6', '7'):
            print('Пожалуйста, выберите 1, 2, 3, 4, 5, 6 или 7')
            input_ = input('\nВыберите действие(введите индекс): ')
        index_choose = int(input_[0])
        function = self.menu_dict[self.menuList[index_choose - 1]]
        function()
