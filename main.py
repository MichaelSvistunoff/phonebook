from ProjectStructure.UI.App import App


class Main():

    def __init__(self):
        self.application = App()


if __name__ == '__main__':
    #     # try:
    #     #     with open('phone-book.txt', 'x'):
    #     #         pass
    #     # except FileExistsError:
    #     #     pass
    programm = Main()
    programm.application.menu()
