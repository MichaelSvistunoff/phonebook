from ProjectStructure.Core.Models.Contact import Contact


class PhoneBook():

    def __init__(self):
        self.contact = Contact()
        self._contacts = []

    def add_contact(self):
        print("Adding a new contact:")
        while True:
            user_input = input("Enter a first name: ").title()
            if not user_input:
                break
            self.contact.set_first_name(user_input)
            user_input = input("Enter a middle name: ").title()
            if not user_input:
                break
            self.contact.set_mid_name(user_input)
            user_input = input("Enter a last name: ").title()
            if not user_input:
                break
            self.contact.set_last_name(user_input)
            user_input = input("Enter phone number: ")
            if not user_input:
                break
            self.contact.set_phone_number(user_input)
            try:
                with open('db.txt', 'a', encoding='utf8') as database:
                    data = f"{self.contact.get_last_name()},{self.contact.get_first_name()}," \
                           f"{self.contact.get_mid_name()},{self.contact.get_phone_number()}\n"
                    database.write(data)
                    print(f"The contact '{self.contact.get_first_name()}' was added!\n")
                    pass
            except FileExistsError:
                pass

    def show_all_contacts(self):
        with open('db.txt', 'r', encoding='utf8') as database:
            lines = database.readlines()
            count = 0
            if lines:
                for line in lines:
                    if line:
                        line = line.strip().split(",")
                        print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
                        count += 1
                print(f"\nВ справочнике найдено {count} контактов")
            else:
                print('Пока нету контактов!')

    def search_by_name(self):
        print("Adding a new contact:")
        user_input = None
        while True:
            user_input = input("Input name u wanna find: ")
            if not user_input:
                break
            find = False
            with open('db.txt', 'r', encoding='utf8') as database:
                lines = database.readlines()
                for line in lines:
                    line = line.strip().split(",")
                    if user_input in line[1]:
                        find = True
                        print(f"{line[0]},{line[1]},{line[2]},{line[3]}")
            if not find:
                print('Такой контакт не найден!')