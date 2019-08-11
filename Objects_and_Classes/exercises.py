class Exercise:
    def __init__(self, topic, course_name, judge_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_link = judge_link
        self.problems = problems


def create_excercise(info_list):
    return Exercise(topic=info_list[0], course_name=info_list[1], judge_link=info_list[2], problems=info_list[3].split(', '))


def print_list(some_list):
    for item in range(len(some_list)):
        print(f'{item+1}. {some_list[item]}')


my_excercise = None
exercises_list = []

while True:
    data_list = input().split(' -> ')
    if data_list[0] == 'go go go':
        break

    my_excercise = create_excercise(data_list)
    exercises_list.append(my_excercise)


for each_exercise in exercises_list:
    print(f'Exercises: {each_exercise.topic}')
    print(f'Problems for exercises and homework for the "{each_exercise.course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {each_exercise.judge_link}')
    print_list(each_exercise.problems)