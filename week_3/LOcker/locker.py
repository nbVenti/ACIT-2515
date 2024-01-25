

class Locker:
    def __init__(self, code):
        
        self.locked = False
        self.contents = []
        
        if type(code) != str or len(code) < 3:
            raise AttributeError
        
    
        
    def lock(self):
        self.locked = True  
        
    def unlock(self):
        self.locked = False
        return True
    
    def unlock_with_code(self,code):
        if type(code) != str:
            return False
        elif len(code) > 3:
            if self.unlock():
                return True
        else:
            return False

            
            
        
    def is_empty(self):
        if len(self.contents) == 0:
            return True
        else:
            return False
        