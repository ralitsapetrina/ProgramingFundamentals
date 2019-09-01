start_hours, start_minutes, start_seconds = list(map(int, input().split(':')))
steps_taken = int(input())
seconds_per_step = int(input())
steps_in_seconds = steps_taken * seconds_per_step


def format_time(value, end_point):
    if value >= end_point:
        value -= end_point
    if value < 10:
        return f'0{value}'
    else:
        return f'{value}'

def calc_time(hour, minute, second):
    if second >= 60:
        add_min = second // 60
        minute += add_min
        second %= 60
    if minute >= 60:
        add_hour = minute // 60
        hour += add_hour
        minute %= 60
    second_f = format_time(second, 60)
    minute_f = format_time(minute, 60)
    hour_f = format_time(hour, 24)
    return f'{hour_f}:{minute_f}:{second_f}'

def calc_end_seconds():
    arrival_seconds = steps_in_seconds % 60
    return arrival_seconds + start_seconds

def calc_end_minutes():
    arrival_minutes = steps_in_seconds // 60
    if arrival_minutes > 60:
        arrival_minutes %= 60
    return arrival_minutes + start_minutes

def calc_end_hours():
    arrival_minutes = steps_in_seconds // 60
    if arrival_minutes > 60:
        arrival_hours = arrival_minutes // 60
        if arrival_hours > 24:
            arrival_hours %= 24
    else:
        arrival_hours = 0
    return arrival_hours + start_hours

print(f'Time Arrival: {calc_time(calc_end_hours(), calc_end_minutes(), calc_end_seconds())}')