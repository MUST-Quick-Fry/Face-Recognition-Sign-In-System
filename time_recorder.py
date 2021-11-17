import datetime


def get_time_record():

    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_today():

    return datetime.datetime.now().date()


if __name__ == '__main__':
    print(get_time_record())
    print(get_today())