import matplotlib.pyplot as plt
import numpy as np
from sqlite3Helper import SQLITE3_Helper

sql3_helper = SQLITE3_Helper()

def plotpie():
    sqlcmd = "SELECT * FROM SignIn"
    re = sql3_helper.query(sqlcmd)
    print(re)

    y = np.array([85, 15])

    plt.pie(y,
        labels=['Attendance', 'Absence'],
        colors=["#d5695d", "#a564c9"],
        explode=(0.25, 0),
        autopct='%.2f%%',
    )
    plt.title("Attendance & Absence Rate")
    plt.show()


def plotbar():
    sqlcmd = "SELECT * FROM SignIn"
    re = sql3_helper.query(sqlcmd)
    today = "2021-10-19"
    #print(re)

    # get time record
    record = []
    for each in re:
        if list(each)[3].split()[0] == today:
            s = list(each)[3].split()[1]
            record.append(str(s.split(":")[0]) + ":" + str(s.split(":")[1]))

    #print(record)

    dic = {}
    for key in record:
        dic[key] = dic.get(key, 0) + 1

    #print(dic)

    time = list(dic)
    num = list(dic.values())
    #print(time)
    #print(num)


    # set parameters
    data_num = len(time)
    data_max = max(num)
    fig_width = 8 + 0.5 * data_num
    fig_height = 4 + 0.5 * data_num

    # draw plot
    plt.figure(figsize=(fig_width, fig_height))
    plt.title("Sign-in Record on " + str(today) + "          Total students: " + str(len(num)))
    plt.xlabel("Sign-in Time")
    plt.ylabel("Number of Students")
    plt.ylim(0, 1.2 * data_max)
    plt.yticks([])
    plt.bar(time, num, color=["#707070", "#949494", "#B8B8B8", "#DCDCDC"], width=0.4)

    for a, b in zip(time, num):
        plt.text(a, b + 0.02, '%.0f' % b, ha='center', va='bottom', fontsize=11)

    plt.show()



if __name__ == '__main__':
    #plotpie()
    plotbar()