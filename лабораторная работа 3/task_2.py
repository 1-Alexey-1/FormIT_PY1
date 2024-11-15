# TODO Напишите функцию find_common_participants
def find_common_participants(x, y, z=','):
    a = []
    x = x.split(z)
    y = y.split(z)
    for i in x:
        for j in y:
            if i == j:
                a.append(i)
    a.sort()
    return(a)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))