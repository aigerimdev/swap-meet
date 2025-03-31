import uuid

class Item:
    def __init__(self, id = None):
        if id is None:
           self.id = uuid.uuid4().int 
        else:
            self.id = id
    def get_category(self):
        return "Item"
    #dunder str method to override str()
    def __str__(self):
        return f"An object of type Item with id {self.id}."