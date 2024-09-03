def roll_call_dwarves(dwarf_list):
    i = 0
    while i < len(dwarf_list):
        print(f"{i + 1}. {dwarf_list[i]}")
        i += 1

def summon_captain_planet(planeteer_list):
    return [f"{planeteer.capitalize()}!" for planeteer in planeteer_list]

def long_planeteer_calls(planeteer_list):
    for planeteer in planeteer_list:
        if len(planeteer) < 4:
            return True
        else:
            return False

def find_the_cheese(my_list):
    cheese = ["cheddar", "gouda", "camembert"]
    cheese_in_my_list = [item for item in my_list if item in cheese]
    if cheese_in_my_list:
        return cheese_in_my_list[0]
    return None
