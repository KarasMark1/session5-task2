class member:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        return "Member Name: "+self.name
class staff_member(member):
    def __init__(self, name, staff_id):
        super().__init__(name)
        self.staff_id = staff_id
    def add_book(self, library, book_title):
        '''allows a staff member to add a new book to the library.'''
        library.add_book(book_title)
        return 'staff member '+self.name+' (id: '+self.staff_id+'+ added '+book_title+' to the library.'
    def display_info(self):
        return 'staff member name: '+self.name+', staff id: '+self.staff_id
class library:
    def __init__(self):
        self.books = []
    def add_book(self, book_title):
        self.books.append(book_title)
    def list_books(self):
        return self.books
my_library = library()
staff1 = staff_member("karas", "4444")
print(staff1.display_info())
print(staff1.add_book(my_library, "the great gatsby"))
print(my_library.list_books())