def alarm_time(hh, mm) -> dict:
    if mm >= 45:
        new_hh = hh
        new_mm = mm - 45

    elif hh == 0:
        new_hh = 23
        new_mm = mm + 60 - 45

    else:
        new_hh = hh - 1
        new_mm = mm + 60 - 45

    return {'hh': new_hh, 'mm': new_mm}


if __name__ == '__main__':
    hh, mm = map(int, input().split())
    new_time = alarm_time(hh, mm)
    print(new_time['hh'], new_time['mm'])
