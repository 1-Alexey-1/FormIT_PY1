# TODO Написать свою реализацию функции для подсчёта числа вхождение элементов в список
def my_count(l: list, item):
    count = 0
    for element in l:
        if element == item:
            count += 1
    return count
