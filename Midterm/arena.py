from pokemon import Pokemon
import csv


class Arena:
    def __init__ (self):
        self.arena = []
        self.arena = self.get_pokemons()
        
    def __len__ (self):
        self.arena = self.get_pokemons()
        return len(self.arena)
        
        
    def add(self,pokemon):
        if type(pokemon.name) != str:
            raise AttributeError
        if type(pokemon.health) != int:
            raise AttributeError
        self.arena.append(pokemon)
        
    def get_pokemons(self,):
        alive_mons = []
        for i in self.arena:
            if i.health >= 1:
                alive_mons.append(i)
            
                    
        alive_mons.sort(key=lambda i: i.name)
        return alive_mons
    
    def active(self):
        return self.get_pokemons()
    
    def load_from_file(self,file):
        with open(file,"r") as f:
            file = csv.reader(f)
            for i in file:
                if i[1].isnumeric():
                    i[1]=int(i[1])
                    new = Pokemon(i[0],i[1])
                    self.add(new)