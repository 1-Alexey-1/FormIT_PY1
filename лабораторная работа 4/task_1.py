# TODO решите задачу
def task() -> float:
    x1 = 0
    x2 = 0
    summ = 0
    f = open("input.json", "r")
    a = f.readlines()
    for i in range(len(a)):
        if a[i].find("score") != -1:
            x1 = float(a[i][((a[i].find("score"))+8):len(a[i])-2])
        elif (a[i].find("weight")) != -1:
            x2 = float(a[i][((a[i].find("weight"))+9):len(a[i])-1])
        if(x1 != 0) and (x2 != 0):
            summ += x1*x2
            x1, x2 = 0, 0
    f.close()
    return round(summ, 3)
print(task())
