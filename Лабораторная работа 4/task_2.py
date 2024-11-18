import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    with open(INPUT_FILENAME, 'r', newline='\n') as f:
        data = []
        reader = csv.DictReader(f, delimiter=',')
        for i in reader:
            data.append(i)
        with open(OUTPUT_FILENAME, 'w') as f_1:
            json_data = json.dumps(data, indent=4)
            f_1.write(json_data)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
