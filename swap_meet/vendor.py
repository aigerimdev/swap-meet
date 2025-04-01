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
    def get_by_id(self, given_id):
        for item in self.inventory:
            if given_id == item.id:
                return item
        return None
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            
            self.remove(my_first_item)
            other_vendor.add(my_first_item)
            other_vendor.remove(their_first_item)
            self.add(their_first_item)
            return True
        return False
        