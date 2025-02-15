from datetime import datetime

def get_time():
    print('hh:mm:ss')
    # time1 = input('time 1: ')
    # time2 = input('time 2: ')

    time1 = '11:00:33'
    time2 = '13:05:00'

    time1 = datetime.strptime(time1, '%H:%M:%S')
    time2 = datetime.strptime(time2, '%H:%M:%S')

    # print(time1)
    # print(time2)

    return time1, time2

def get_dif_sec(t1, t2):
    dif = t2 - t1
    return dif.seconds

def get_dif_str(t1, t2):
    dif = t2 - t1
    dif = dif.seconds
    h = dif // 3600
    m = dif // 60 - h * 60  # min - hourmin
    s = dif % 60
    result = f"{h} hours, {m} minutes, {s} seconds"
    return result


try:
    times = get_time()
except ValueError:
    print('invalid date')
else:
    print('dif sec =', get_dif_sec(*times))
    print('dif str =', get_dif_str(*times))