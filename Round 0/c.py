def get_input():
    line         = input().split()
    hour, minute = map(int, line[:2])
    is_AM        = line[2] == 'AM'
    return hour, minute, is_AM

def convert(time, kut, is_from):
    hour, minute, is_AM = time
    if hour == 12:
        hour -= 12
    
    if not is_AM:
        hour += 12
    
    if is_from:
        hour   -= kut[0]
        minute -= kut[1]
    else:
        hour   += kut[0]
        minute += kut[1]
    
    if minute > 59:
        minute -= 60
        hour   += 1
    elif minute < 0:
        minute += 60
        hour   -= 1
    
    if hour < 0:
        hour += 24
    elif hour > 23:
        hour -= 24

    is_AM = True
    if hour > 11:
        hour -= 12
        is_AM = False
    
    if hour == 0:
        hour += 12
    return hour, minute, is_AM

if __name__ == '__main__':
    time         = convert(get_input(), (8, 0), True)
    hour, minute = map(int, input().split())

    hour, minute, is_AM = convert(time, (hour, minute), False)
    meridian            = 'AM' if is_AM else 'PM'
    print(f'{hour} {minute} {meridian}')