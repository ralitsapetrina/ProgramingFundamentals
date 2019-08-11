class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        f_n = f'First Name: {self.first_name}'
        l_n = f'Last Name: {self.last_name}'
        return f'{f_n}\n{l_n}'

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if value[0].islower():
            raise Exception(f'Expected upper case letter! Argument: firstName')
        elif len(value) <= 3:
            raise Exception(f'Expected length at least 4 symbols! Argument: firstName')
        else:
            self.__first_name = value


    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if value[0].islower():
            raise Exception(f'Expected upper case letter! Argument: lastName')
        elif len(value) <= 2:
            raise Exception(f'Expected length at least 3 symbols! Argument: lastName')
        else:
            self.__last_name = value


class Student(Human):
    def __init__(self, first_name, last_name, faculty_num):
        Human.__init__(self, first_name, last_name)
        self.faculty_num = faculty_num

    def __str__(self):
        names = Human.__str__(self)
        fac_num = f'Faculty number: {self.faculty_num}'
        return f'{names}\n{fac_num}'

    @property
    def faculty_num(self):
        return self.__faculty_num

    @faculty_num.setter
    def faculty_num(self, value):
        for item in value:
            if item.isdigit() or item.isalpha():
                continue
            else:
                raise Exception('Invalid faculty number!')
        if len(value) < 5 or len(value) > 10:
            raise Exception('Invalid faculty number!')
        else:
            self.__faculty_num = value

class Worker(Human):
    def __init__(self, first_name, last_name, week_salary, day_hours):
        Human.__init__(self, first_name, last_name)
        self.week_salary = week_salary
        self.day_hours = day_hours

    def calc_hour_money(self):
        work_days = 5
        hour_money = self.week_salary / (work_days * self.day_hours)
        return hour_money

    def __str__(self):
        names = Human.__str__(self)
        week_sal = f'Week Salary: {self.week_salary:.2f}'
        h_per_day = f'Hours per day: {self.day_hours:.2f}'
        sal_per_h = f'Salary per hour: {self.calc_hour_money():.2f}'
        return f'{names}\n{week_sal}\n{h_per_day}\n{sal_per_h}'

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, value):
        if value <= 10:
            raise Exception(f'Expected value mismatch! Argument: weekSalary')
        else:
            self.__week_salary = value

    @property
    def day_hours(self):
        return self.__day_hours

    @day_hours.setter
    def day_hours(self, value):
        if value < 1 or value > 12:
            raise Exception(f'Expected value mismatch! Argument: workHoursPerDay')
        else:
            self.__day_hours = value


try:
    student_input = input().split()
    student = Student(first_name=student_input[0], last_name=student_input[1], faculty_num=student_input[2])
    worker_input = input().split()
    worker = Worker(first_name=worker_input[0], last_name=worker_input[1], week_salary=float(worker_input[2]), day_hours=float(worker_input[3]))
    print(student, '\n')
    print(worker)
except Exception as e:
    print(str(e))