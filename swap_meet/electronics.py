import uuid
class Electronics:
    def __init__(self, id=None, type=None, condition=None):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        if type is None:
            self.type = "Unknown"
        else:
            self.type = type
            
        if condition is None:
            self.condition = 0
        else:
            self.condition = condition
    
    def get_category(self):
        return "Electronics"
    
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
    
    def condition_description(self):
        if self.condition >= 0 and self.condition < 2:
            return "heavily used"
        if self.condition >= 2 and self.condition < 4:
            return "fair"
        else:
            return "good"