'''
Your manager noticed that there's a lot of repetitive code in the "Age of Dragons" code base. 
She asked you to update the fight_soldiers function so that the DPS (damage-per-second) calculation is only written once.
Create a new function called get_soldier_dps that takes a soldier and returns its DPS using the same logic as the lines above. 
Then, replace the two lines above with calls to get_soldier_dps.
'''

##original function
def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"

##my get soldier dps function
def get_soldier_dps(solider: dict[str:int, str:int]) -> int:
    return(solider["damage"] * solider["attacks_per_second"])

##my updated function
def fight_soldiers(soldier_one: dict[str:int, str:int], soldier_two: dict[str:int, str:int]) -> str:
    soldier_one_dps:int = get_soldier_dps(soldier_one)
    soldier_two_dps:int = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"