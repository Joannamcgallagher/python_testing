from datetime import date, timedelta

class Student:
    """ A Student Class as base for nethod testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        # An underscore on front of the fields above are to say that that field is read only
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"    