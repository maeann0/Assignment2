from Item import item

class book(item):

    # Attributes
    ISBN = 0
    Author = ''
    Synopsis = ''

    # Methods
    def preview(self):
        print(f"Previewing{self.Title} by {self.Author}:\n{self.Synopsis}")