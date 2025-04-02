import uuid
from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, width = None, length=None, condition = None):
        super().__init__(id, condition)            
        if width is None:
            self.width = 0
        else:
            self.width = width     
        if length is None:
            self.length = 0    
        else:
            self.length = length
        

    def __str__(self):
        item_summary = super().__str__()
        decor_summary = f"It takes up a {self.width} by {self.length} sized space."
        return " ".join((item_summary, decor_summary))