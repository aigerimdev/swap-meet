class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory
    def add(self, item):
        self.inventory.append(item)
        return item
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False