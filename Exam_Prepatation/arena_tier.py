class Gladiator:
    def __init__(self, gladiator, techniques: dict):
        self.gladiator = gladiator
        self.techniques = techniques

    def calc_total_skill(self):
        skills_list = map(lambda x: self.techniques.get(x), self.techniques)
        return sum(skills_list)

    def format_skills(self):
        string_list = []
        for k, v in self.techniques.items():
            string_list.append(f'- {k} <!> {v}')
        return string_list

    def __str__(self):
        intro = f'{self.gladiator}: {self.calc_total_skill()} skill'
        list_print = '\n'.join(self.format_skills())
        return f'{intro}\n{list_print}'

gladiators_dict = {}

def update_gladiator(data_list):
    name = data_list[0]
    skill_dict = {data_list[1]: int(data_list[2])}
    if not name in gladiators_dict:
        gladiator = Gladiator(name, skill_dict)
        gladiators_dict[name] = gladiator
    else:
        gladiator_ex = gladiators_dict.get(name)
        if data_list[1] in gladiator_ex.techniques:
            if  data_list[2] < gladiator_ex.techniques.get(data_list[1]):
                gladiator_ex.techniques[data_list[1]] = int(data_list[2])
        else:
            gladiator_ex.techniques[data_list[1]] = int(data_list[2])



while True:
    data_list = input().split(' -> ')
    if data_list[0] == 'Ave Cesar':
        break
    update_gladiator(data_list)

print(gladiators_dict)

