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
            return self.swap_items(other_vendor, my_first_item, their_first_item)      
        return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category

    def get_best_by_category(self, category):
        items_list = self.get_by_category(category)
        if len(items_list) == 0:
            return None
        highest_condition_item = items_list[0]
        for item in items_list:
            if item.condition > highest_condition_item.condition:
                highest_condition_item = item
        return highest_condition_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_from_my_inv = self.get_best_by_category(their_priority)
        item_from_their_inv = other_vendor.get_best_by_category(my_priority)
        if item_from_my_inv == None or item_from_their_inv == None:
            return False
        return self.swap_items(other_vendor, item_from_my_inv, item_from_their_inv)