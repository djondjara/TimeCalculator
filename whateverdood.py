def time_split(time):

    hours_and_minutes = time.split(":")

    hours_str = hours_and_minutes[0]
    hours = int(hours_str)
    minutes_str = hours_and_minutes[1]
    minutes = int(minutes_str)

    return hours, minutes


def day_change(day, days_past):

    day_after = 0
    Weekend = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "SaturDay", "Sunday"]
    Weekend_len = len(Weekend)

    matching_indices = []
    for current_day, item in enumerate(Weekend):
        if item == day:
            matching_indices.append(current_day)
            day_after = days_past + current_day
            while day_after > 7:
                day_after -= 7

    return Weekend[day_after]
