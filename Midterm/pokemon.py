class Pokemon:
    def __init__(self, mon, health):
        if type(mon) != str:
            raise ValueError
        if type(health) != int:
            raise ValueError
        if (health <= 0):
            raise ValueError
        self.name = mon
        self.health = health
        self.level = 1
        
    def level_up(self):
        self.level += 1
        
    def join(self,arena):
        arena.add(self)
        pass