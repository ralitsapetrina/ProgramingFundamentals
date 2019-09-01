class Wizard:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def print_wizard(self):
        return f'Wizard: {self.name}. Health: {self.health}. Damage power: {self.damage}'


wizards_dict = {}

def fighting(attacker, attacked):
    attacked.health -= attacker.damage
    attacker.health += 50
    if attacked.health <= 0:
        print(f'Fatality - {attacker.name} wins!')
        return True
    else:
        print(f'Next time {attacked.name}!')
        return False

while True:
    wizarding = input().split()
    command = wizarding[0]
    if command == 'fight':
        break
    name = wizarding[1]
    health = int(wizarding[2])
    damage = int(wizarding[3])

    if command == 'new':
        if not name in wizards_dict.keys():
            new_wizard = Wizard(name=name, health=health, damage=damage)
            wizards_dict[name] = new_wizard
        else:
            print('Wizard already exists!')
    elif command == 'edit':
        if name in wizards_dict.keys():
            wizard = wizards_dict.get(name)
            wizard.health += health
            wizard.damage += damage
        else:
            print('Wizard does not exist!')

while True:
    fighters = input().split(' <=> ')
    if fighters[0] == 'end':
        break
    if fighters[0] in wizards_dict.keys() and fighters[1] in wizards_dict.keys():
        is_dead = fighting(wizards_dict.get(fighters[0]), wizards_dict.get((fighters[1])))
        if is_dead:
            del wizards_dict[fighters[1]]
    else:
        print('Cannot place a fight with non-existing wizards!')

sorted_wizards = list(sorted(wizards_dict, key=lambda x: wizards_dict.get(x).health, reverse=True))

for wizard in sorted_wizards:
    print(wizards_dict.get(wizard).print_wizard())