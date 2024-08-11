'''
Add a fortify() method to your wall class. It should double the current armor property.
'''

class Wall:
    armor = 10
    height = 5

    def fortify(self) -> None:
        self.armor = self.armor*2