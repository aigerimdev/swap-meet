import uuid

class Item:
    def __init__(self, id=None, condition=None):
        if id is None:
           self.id = uuid.uuid4().int 
        else:
            self.id = id
        self.condition = condition if condition is not None else 0

           
    def get_category(self):
        return self.__class__.__name__
    
    # dunder str method to override str()
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        if self.condition >= 0 and self.condition < 2:
            return "heavily used"
        if self.condition >= 2 and self.condition < 4:
            return "fair"
        else:
            return "good"