class Contact():
    def __init__(self, first_name=None, last_name=None, mid_name=None, phone_number=None):
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._mid_name = mid_name
        self._phone_number = phone_number

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_mid_name(self):
        return self._mid_name

    def set_mid_name(self, mid_name):
        self._mid_name = mid_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
