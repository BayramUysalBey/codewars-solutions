'''Enjoying your holiday, you head out on a scuba diving trip!

Disaster!! The boat has caught fire!!

You will be provided a string that lists many boat related items. If any of these items are "Fire" you must spring into action. Change any instance of "Fire" into "~~". Then return the string.'''

# My solution
def fire_fight(s):
    s_s = s.split()
    result = []
    for word in s_s:
        if word.lower() == "fire": result.append("~~")
        else: result.append(word)
    return " ".join(result)

# My updated solution
def fire_fight(s):
    return s.replace("Fire", "~~")
       