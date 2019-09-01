decrypt_key = input()

class Football_team:
    def __init__(self, name, points, goals):
        self.name = name
        self.points = points
        self.goals = goals

    def print_points(self):
        return f'{self.name} {self.points}'

    def print_goals(self):
        return f'{self.name} -> {self.goals}'

def define_points(team_a, team_b):
    if team_a > team_b:
        team_a_points = 3
        team_b_points = 0
    elif team_a < team_b:
        team_a_points = 0
        team_b_points = 3
    else:
        team_a_points = 1
        team_b_points = 1

    return[team_a_points, team_b_points]

team_dict = {}

while True:
    input_list = input().split()
    if input_list[0] == 'final':
        break
    team_a_reversed = (input_list[0].split(decrypt_key))[1]
    team_a = team_a_reversed[::-1].upper()
    team_b_reversed = (input_list[1].split(decrypt_key))[1]
    team_b = team_b_reversed[::-1].upper()
    team_a_goals, team_b_goals = list(map(int, input_list[2].split(':')))

    team_a_points, team_b_points = define_points(team_a_goals, team_b_goals)

    if not team_a in team_dict:
        create_team_a = Football_team(team_a, team_a_points, team_a_goals)
        team_dict[team_a] = create_team_a
    else:
        team_dict.get(team_a).points += team_a_points
        team_dict.get(team_a).goals += team_a_goals

    if not team_b in team_dict:
        create_team_b = Football_team(team_b, team_b_points, team_b_goals)
        team_dict[team_b] = create_team_b
    else:
        team_dict.get(team_b).points += team_b_points
        team_dict.get(team_b).goals += team_b_goals

sorted_points = sorted(team_dict, key=lambda x: (- team_dict.get(x).points, team_dict.get(x).name))
sorted_goals = sorted(team_dict, key=lambda x: (- team_dict.get(x).goals, team_dict.get(x).name))


print('League standings:')
for ind in range(1, len(sorted_points) + 1):
    get_value = team_dict.get(sorted_points[ind-1])
    print(f'{ind}. {get_value.print_points()}')
print('Top 3 scored goals:')
for ind in range(3):
    if len(sorted_goals) < 3:
        if ind > len(sorted_goals) - 1:
            break
    get_value = team_dict.get(sorted_goals[ind])
    print(f'- {get_value.print_goals()}')