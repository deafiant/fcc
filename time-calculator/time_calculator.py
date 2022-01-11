def add_time(start, duration, day=None):
    """
    
    """
    
    start_time, start_ampm = start.split()
    start_hour, start_min = start_time.split(":")
    dur_hour, dur_min = duration.split(":")

    new_hour = int(start_hour) + int(dur_hour)
    new_min = int(start_min) + int(dur_min)
    if start_ampm == "PM":
        new_hour += 12
    if new_min >= 60:
        new_min = new_min % 60
        new_hour += 1
    add_days = new_hour // 24
    new_hour = new_hour % 24
    new_ampm = "AM"
    if new_hour == 12:
        new_ampm = "PM"
    elif new_hour > 12:
        new_hour -= 12
        new_ampm = "PM"
    elif new_hour == 0:
        new_hour = 12
    extra = ""
    if add_days == 1:
        extra = " (next day)"
    elif add_days > 1:
        extra = f" ({add_days} days later)"
    days_of_week = ["monday", "tuesday", "wednesday",
                    "thursday", "friday", "saturday", "sunday"]
    if day:
        if day.lower() in days_of_week:
            day_index = days_of_week.index(day.lower())
            day_index += add_days
            new_day = days_of_week[day_index % 7]
            extra = f", {new_day.capitalize()}" + extra
        else:
            return f"Error: '{day}' is not a day of the week."


    return f"{new_hour}:{new_min:02} {new_ampm}{extra}"

if __name__ == "__main__":
    print("11:26 AM + 2:12 is ", add_time("11:26 AM", "2:12"))
    print("11:30 AM + 1:00 is ", add_time("11:30 AM", "1:00"))
    print("11:15 PM + 1:40 is ", add_time("11:15 PM", "1:40"))
    print("8:26 AM + 55:09 is ", add_time("8:26 AM", "55:09"))
    print("10:35 pm Sunday + 14:40 is ", add_time("10:35 pm", "14:40", "Sunday"))
    print("10:35 pm boo + 14:40 is ", add_time("10:35 pm", "14:40", "boo"))