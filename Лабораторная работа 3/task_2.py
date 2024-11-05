# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    first_group, second_group = set(first_group.split(separator)), set(second_group.split(separator))
    common_participants = sorted(list(first_group.intersection(second_group)))
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator='|'))
