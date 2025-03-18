from sys import maxsize


class Contact:
    """1.  Конструктор: __init__ является конструктором класса.
2.  Параметры по умолчанию: Все параметры имеют значения по умолчанию None, поэтому они необязательные.
3.  Атрибуты объекта: Значения, переданные в конструктор, присваиваются атрибутам объекта, которые затем можно использовать.
4.  Гибкость: Вы можете создавать объекты с различными наборами свойств.

Что это дает:

1.  Создание объектов: Позволяет создавать новые объекты с заданными свойствами.
2.  Начальная инициализация: Позволяет задать начальные значения свойств объекта при его создании.
3.  Гибкость: Позволяет создавать объекты с разными наборами данных.
4.  Инкапсуляция: Позволяет инкапсулировать данные в объектах, что делает код более организованным.

В заключение:

Этот код — это стандартный способ определения конструктора класса в Python. Он позволяет создавать объекты с нужными вам свойствами и начальными значениями."""
    def __init__(self, firstname=None, lastname=None, id=None, all_phones_from_page=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_page = all_phones_from_page
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
