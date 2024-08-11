'''
Complete the Wizard class's constructor. It should set 2 private properties:

"stamina"
"intelligence"
Don't forget to make them private! Use the values passed into the constructor to set the properties.

It should also set 3 public properties:

name: Use the value passed into the constructor.
health: 100x the value of "stamina".
mana: 10x the value of "intelligence".
'''

class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.name = name
        self.health = 100 * stamina
        self.mana = 10 * intelligence