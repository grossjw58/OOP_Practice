'''
Add a .get_cost() method to your wall class. 
What do you think it should return? The cost of a wall is the product of its height and armor:
'''
class Wall:
    armor: int = 10
    height: int = 5

    def get_cost(self) -> int:
        return(self.armor * self.height)

    # don't touch below this line
    def fortify(self):
        self.armor *= 2