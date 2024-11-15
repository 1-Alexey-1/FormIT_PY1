# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    x = open(INPUT_FILENAME, "r")
    y = open(OUTPUT_FILENAME, "w")
    reader = csv.DictReader(x)
    z = []
    for i in reader:
        z.append(i)

    json.dump(z, y, indent = 4)
    y.close()
    x.close()


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
