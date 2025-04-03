import uuid
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, id=None, fabric=None, condition=None):
        super().__init__(id, condition)
        if fabric is None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric

    def __str__(self):
        item_summary = super().__str__()
        fabric_summary = f"It is made from {self.fabric} fabric."
        return " ".join((item_summary, fabric_summary))