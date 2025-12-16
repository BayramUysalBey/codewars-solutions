"""Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0."""

# My solution
def combat(health, damage):
    res = health - damage
    if res > 0:
        return res
    elif res <= 0:
        return 0

# My updated solution
def combat(health, damage):
    return health - damage if health > damage else 0