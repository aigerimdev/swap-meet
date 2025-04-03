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
        condition={
            0: "bad",
            1: "heavily used",
            2: "used",
            3: "fair",
            4: "very good",
            5: "like new"        
        }
        if self.condition in condition:
            return condition[self.condition]