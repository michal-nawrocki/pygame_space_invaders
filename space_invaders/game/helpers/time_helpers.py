

def has_time_passed(current_time, last_time, delay):
    if last_time == 0:
        return True
    elif current_time - last_time >= delay:
        return True
    else:
        return False
