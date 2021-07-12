

class Nutrient_Object:

    # constructor
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit

    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def get_unit(self):
        return self.unit
    
    def get_nutrient(self):
        return [self.name, self.value, self.unit]