import uuid
from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type=None, condition=None):
        super().__init__(id, condition)
        if type is None:
            self.type = "Unknown"
        else:
            self.type = type
   
    def __str__(self):
        item_summary = super().__str__()
        electronics_summary = f"This is a {self.type} device."
        return " ".join((item_summary, electronics_summary))