# TODO решите задачу
import json
INPUT_FILENAME = 'input.json'


def task() -> float:
    with open(INPUT_FILENAME, 'r') as f:
        data = json.load(f)
        sum_ = 0.0
        for i in data:
            sum_ += i['score'] * i['weight']
        return round(sum_, 3)


print(task())
