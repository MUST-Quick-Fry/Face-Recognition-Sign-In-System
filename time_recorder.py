import time

def get_time_record():
    localtime = time.localtime(time.time())
    # print("本地时间为 :", localtime)

    hour = str(localtime.tm_hour)
    minu = str(localtime.tm_min)
    sec = str(localtime.tm_sec)

    if localtime.tm_hour < 10:
        hour = str(0) + hour

    if localtime.tm_min < 10:
        minu = str(0) + minu

    if localtime.tm_sec < 10:
        sec = str(0) + sec

    time_record = str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(localtime.tm_mday) + " " + hour + ":" + minu + ":" + sec

    return time_record


def get_today():
    localtime = time.localtime(time.time())

    today_record = str(localtime.tm_year) + "-" + str(localtime.tm_mon) + "-" + str(localtime.tm_mday)

    return today_record


if __name__ == '__main__':
    print(get_time_record())