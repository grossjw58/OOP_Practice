'''
Finish the shoot method. It takes an Archer instance as the target input.
If the shooter has no arrows left, raise the exception {} can't shoot where {} is the shooter's name. 
Otherwise, remove an arrow from the shooter and print {1} shoots {2} where {1} is the shooter's name 
and {2} is the name of the targeted archer. 
Next, call the target's get_shot() method.
'''
##original
class Archer_old:
    def __init__(self, name, health, num_arrows):
        pass

    def get_shot(self):
        pass

    def shoot(self, target):
        pass

    # don't touch below this line
    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

##updated
class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def get_shot(self):
        if self.health <= 1:
            self.health = 0
            raise Exception(f"{self.name} is dead")
        else:
            self.health -= 1


    def shoot(self, target):
        if self.num_arrows > 0:
            self.num_arrows -= 1
            print(f"{self.name} shoots {target.name}")
            target.get_shot()
        else:
            raise Exception(f"{self.name} can't shoot")

    # don't touch below this line
    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")