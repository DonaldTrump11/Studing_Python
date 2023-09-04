class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError("Читать моно только книги")

    def write(self, page, text):
        raise NotImplementedError("Запись можно делать только в NoteBook")


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        super().__init__(title, content)
        #self.type_book = "Novel"
        self.author = author
        self.year = year
        

    def read(self, page):
        """возвращает страницу"""
        print(" Команда выполняется, читаем файл))")

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
    
    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise NotImplementedError("Запись (write] можно делать только в NoteBook")


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size, max_sign, content=None):
        """конструктор"""
        super().__init__(title, content, size)
        #self.type_book = "Notebook"
        self.max_sign = max_sign
        

    def read(self, page):
        """возвращает страницу с номером page"""
        raise NotImplementedError("Команду READ можно делать только в Novel")

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        print("Команда выполняется, делаем запись))")


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
    
    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        pass
    
    def del_bookmark(self, book):
        """удаляет закладку из книги book"""


------------------------------------------------------
-----------------------------------------------------


-----------------------------------------------------
-----------------------------------------------------

a = Novel("Толстой", "1824", "Война и мир")
print(a.author)
print(a.year)
print(a.title)
print(a.content)
a.read("12")
a.write("3", "Нужный фрагмент текста")


a = Notebook("Война и мир", "233","1000", "На краю дороги стоял дуб")
print(a.size)
print(a.max_sign)
print(a.title)
print(a.content)
a.write("3", "Нужный фрагмент текста")
a.read("12")
