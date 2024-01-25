

class Evo:
    def __init__(self):
        self.driver = None
        self.distance = 0
    
    def start_rental(self, driver):
        if self.driver is None:
            self.driver = driver
        else:
            raise RuntimeError
    
    def drive(self, distance):
        
        if distance <= -1:
            raise AttributeError
        if self.driver is None:
            raise RuntimeError
        else:
            self.distance += distance
    
    def end_rental(self):
        if self.driver is None:
            raise RuntimeError
        total_distance = self.distance
        self.driver = None
        self.distance = 0
        return total_distance
        
        