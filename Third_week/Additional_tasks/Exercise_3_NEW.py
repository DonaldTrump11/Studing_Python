class Book:
    def __init__(self, title, content=None):
        self.title = str(title)
        self.content = content or []
        if not(isinstance(self.content, list)):
            raise TypeError("атрибут Content должен быть тип List))")
        self.size = len(self.content)

    def read(self, page):
        try:
            print(self.content[int(page)-1])
        except:
            raise PageNotFoundError("Прочитать страницу не получается. Нет такой страницы или другая ошибка((")

    def write(self, page, text):
        #raise NotImplementedError("Запись можно делать только в NoteBook))")
        pass


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, author, year, title, content=None):
        """конструктор"""
        super().__init__(title, content)
        # self.type_book = "Novel"
        self.author = str(author)
        self.year = int(year)

    #def read(self, page):
     #   """возвращает страницу"""
      #  #print(" Команда выполняется, читаем файл))")
       # 
        #try:
         #   print(self.content[int(page)-1])
        #except:
         #   raise NotImplementedError("Прочитать страницу не получается. Нет такой страницы или другая ошибка((")

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""

    def write(self, page, text):
        """делает запись текста text на страницу page """
        raise NotImplementedError("Запись-Write можно делать только в NoteBook")


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size=12, max_sign=2000, content=None):
        """конструктор"""
        super().__init__(title, content)
        self.max_sign = int(max_sign)
        if len(self.content)!=0 and len(self.content)!=None :
            self.size = len(content)
        else :
            content = []
            self.size = int(size)
            i = 0
            while i < self.size:
                content.append([])
                i +=1
            self.content = content

    #def read(self, page):
    #    """возвращает страницу с номером page"""
     #   raise NotImplementedError("Команду READ можно делать только в Novel")

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """
        #print("Команда выполняется, делаем запись))")
        
        try:
            if str(self.content[int(page)-1])!="[]":
                self.content[int(page)-1] = self.content[int(page)-1] + str(text)
            else:
                self.content[int(page)-1] = str(text)
        except:
            raise NotImplementedError("Запись сделать не получается. Нет такой страницы или другая ошибка.((")


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""
        self.book = book
        self.page = page
        book(page)

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        pass

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""
        
        
        
        
        
        
        
______________________________________________________________

ds = ["5","3","2"]

a = Notebook("Война и мир", "233","1000", ds)
print(a.title)
print(a.size)
print(a.max_sign)
print(a.content)

________________________________________________________________

ds = ["Страница1","Страница2","Страница3", "Страница4", "Страница5", "Страница6", "Страница7"]

a = Novel("Толстой", "1824", "Война и мир")
print(a.author)
print(a.year)
print(a.title)
print(a.content)
a.read("12")
a.write("3", "Нужный фрагмент текста")


a = Notebook("Война и мир", "233","1000", ds)
print(a.title)
print(a.size)
print(a.max_sign)
print(a.content)
print("_"*25)
a.read("3")
a.write(3, " Нужный фрагмент текста")
a.read("3")
print("_"*25)


