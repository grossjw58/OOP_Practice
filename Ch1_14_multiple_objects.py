'''
Take a look at the Brawler class and the fight function provided. In the main function, create 4 new brawlers with the following stats:
Name: Aragorn. Speed: 4. Strength: 4.
Name: Gimli. Speed: 2. Strength: 7.
Name: Legolas. Speed: 7. Strength: 7.
Name: Frodo. Speed: 3. Strength: 2.
Then call fight twice. The first fight should be Aragorn vs Gimli. The second will be Legolas vs Frodo.
'''

def main() -> None:
    aragorn: Brawler = Brawler(speed = 4, strength = 4, name = "Aragorn")
    gimli: Brawler = Brawler(speed = 2, strength = 7, name = "Gimli")
    legolas: Brawler = Brawler(speed = 7, strength = 7, name = "Legolas")
    frodo: Brawler = Brawler(speed = 3, strength = 2, name = "Frodo")

    fight(f1 = aragorn, f2 = gimli)
    fight(f1 = legolas, f2 = frodo)

# don't touch below this line
class Brawler:
    def __init__(self, speed, strength, name):
        self.speed = speed
        self.strength = strength
        self.power = speed * strength
        self.name = name

def fight(f1, f2):
    if f1.power > f2.power:
        print(f"{f1.name} wins with {f1.power} power over {f2.name}'s {f2.power}")
    elif f1.power < f2.power:
        print(f"{f2.name} wins with {f2.power} power over {f1.name}'s {f1.power}")
    else:
        print(f"It's a tie with both contestants at {f1.power} power")

main()