from whateverdood import time_split
from whateverdood import day_change

def add_time(start, duration, day=None):
    # Splits the start string into time and AM/PM strings
    global next_day
    time_PMorAM = start.split()
    start_time = time_PMorAM[0]
    PMorAM = time_PMorAM[1]

    # Turns string time into integers and calculates new time
    start_hours, start_minutes = time_split(start_time)
    duration_hours, duration_minutes = time_split(duration)

    if PMorAM == "PM":
        new_hours = start_hours + duration_hours + 12
    else:
        new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes

    # Transforms 60 minutes into 1 hour
    if new_minutes > 59:
        new_hours += 1
        new_minutes -= 60
    if new_minutes < 10:
        new_minutes = "0" + str(new_minutes)

    # Number of days
    days_counter = new_hours // 24
    next_day = False

    current_day = day_change(day, days_counter)
    if days_counter > 0:
        new_hours -= 24 * days_counter

        if new_hours > 12:
            new_hours -= 12
            if PMorAM == "AM":
                PMorAM = "PM"
        elif new_hours == 12:
            if PMorAM == "AM":
                PMorAM = "PM"
        elif PMorAM == "PM" and new_hours == 0:
            PMorAM = "AM"
            new_hours += 12
        elif PMorAM == "PM" and new_hours < 12:
            PMorAM = "AM"


    else:
        # Checks if AM and PM should switch
        if new_hours > 12:
            new_hours -= 12
            if PMorAM == "AM":
                PMorAM = "PM"
        elif new_hours == 12:
            if PMorAM == "AM":
                PMorAM = "PM"

    new_time = 0
    if days_counter == 0:

        # Checks if there is a third argument
        if day is not None:
            if next_day:
                new_time = f"{new_hours}:{new_minutes} {PMorAM}, {current_day} (next day)"
            else:
                new_time = f"{new_hours}:{new_minutes} {PMorAM}, {current_day}"
        else:
            if next_day:
                new_time = f"{new_hours}:{new_minutes} {PMorAM} (next day)"
            else:
                new_time = f"{new_hours}:{new_minutes} {PMorAM}"

    elif days_counter == 1:

        # Checks if there is a third argument
        if day is not None:
            new_time = f"{new_hours}:{new_minutes} {PMorAM}, {current_day} (next day)"
        else:
            new_time = f"{new_hours}:{new_minutes} {PMorAM} (next day)"

    else:
        # Checks if there is a third argument
        if day is not None:
            new_time = f"{new_hours}:{new_minutes} {PMorAM}, {current_day} ({days_counter} days later)"
        else:
            new_time = f"{new_hours}:{new_minutes} {PMorAM} ({days_counter} days later)"

    return new_time