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


    new_time = f"{new_hour}:{new_min:02} {new_ampm}{extra}"

    return new_time

if __name__ == "__main__":
    print("1:38 PM,  ", add_time("11:26 AM", "2:12"))
    print("12:30 PM,  ", add_time("11:30 AM", "1:00"))
    print("12:15 AM,  ", add_time("11:15 PM", "1:00"))
    print(add_time("8:26 AM", "55:09"))
    print(add_time("10:35 pm", "14:40", "Sunday"))