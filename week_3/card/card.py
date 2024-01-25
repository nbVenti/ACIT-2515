class Card:
    def __init__(self, value, color):
        try: 
            value = int(value)
        except:
            raise AttributeError
        
        if (value) not in range(1, 11):
            raise AttributeError
        if color not in ['red', 'black']:
            raise AttributeError
        self.value = int(value)
        self.color = color
    
    def is_stronger_than(self, card):
        if self.value > card.value:
            return True
        else:
            return False
        