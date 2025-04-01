import uuid
class Decor:
    def __init__(self, id = None, width = None, length=None, condition = None):
        if id is None:
            self.id = uuid.uuid4().int 
        else:
            self.id = id
            
        if width is None:
            self.width = 0
        else:
            self.width = width
        
        if length is None:
            self.length = 0    
        else:
            self.length = length
        
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
        
    def get_category(self):
        return "Decor"
    
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."
    
    def condition_description(self):
        if self.condition >= 0 and self.condition < 2:
            return "heavily used"
        if self.condition >= 2 and self.condition < 4:
            return "fair"
        else:
            return "good"