import uuid
class Clothing:
    def __init__(self, id = None, fabric = None):
        if id is None:
            self.id = uuid.uuid4().int 
        else:
            self.id = id
        if fabric is None:
           self.fabric = "Unknown"
        else:
            self.fabric = fabric
    def get_category(self):
        return "Clothing"    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."