def add_time(start, duration, day_of_week=False):
    week_days_index = {"monday": 0, "tuesday": 1, "wednesday": 2,
                       "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}

    week_days_array = ["Monday", "Tuesday", "Wednesday",
                       "Thursday", "Friday", "Saturday", "Sunday"]

    duration_hours, duration_minutes = map(int, duration.split(":"))

    start_time = start[:-2]
    start_hours, start_minutes = map(int, start_time.split(":"))
    am_pm = start[-2:]

    ampm_flip = {"AM": "PM", "PM": "AM"}

    day_amount = int(duration_hours / 24)
    end_minutes = start_minutes + duration_minutes

    if (end_minutes >= 60):
        start_hours += 1
        end_minutes %= 60

    amount_ampmflip = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    end_minutes = end_minutes if end_minutes > 9 else str(end_minutes).zfill(2)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours

    if (am_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
        day_amount += 1

    am_pm = ampm_flip[am_pm] if amount_ampmflip % 2 == 1 else am_pm
    returntime = f"{end_hours}:{end_minutes} {am_pm}"

    if (day_of_week):
        day_of_week = day_of_week.lower()
        index = int((week_days_index[day_of_week]) + day_amount) % 7
        new_day = week_days_array[index]

        returntime += ", " + new_day

    if (day_amount == 1):
        return f"{returntime} (next day)"
    elif (day_amount > 1):
        return f"{returntime} ({day_amount} days later)"

    return returntime


add_time("11:06 PM", "2:02")
