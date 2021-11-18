from datetime import datetime


def get_time_record():

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_today():

    return datetime.now().date()


def is_class_time(start_time, end_time):
    """start_time and end_time should be formed as 11:00:00"""
    today = datetime.now().date()
    start_time = str(today) + " " + start_time
    end_time = str(today) + " " + end_time

    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    #print(start, end)

    if start < datetime.now() < end:
        return True
    else:
        return False


if __name__ == '__main__':
    print(get_time_record())
    print(get_today())

    start = "03:00:00"
    end = "05:00:00"
    print(is_class_time(start, end))