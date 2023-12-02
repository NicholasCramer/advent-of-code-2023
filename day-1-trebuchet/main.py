import pandas
import re

# ----------------------------- Part 1 ------------------------------------------
data = pandas.read_csv("puzzle_input.csv")
num_list = []
calibration_values = []
total = 0

data_dict = data.to_dict('list')

# row_list = [i for i in data_dict['data']]
#
# for string in row_list:
#     num_list.append(re.findall(f'[\d+]', string))
#
# for index in num_list:
#
#     if len(index) == 1:
#         calibration_values.append(index[0] + index[0])
#     else:
#         calibration_values.append(index[0] + index[-1])
#
# for num in calibration_values:
#     total += int(num)
# print(total)

# ------------------------------------ Part 2 -----------------------------------

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

new_num_list = []

calibration_values.clear()
for num_str in data_dict['data']:
    for index, char in enumerate(num_str):
        if char.isdigit():
            new_num_list.append(char)
        elif isinstance(char, str):
            for num_idx, num in enumerate(numbers.keys()):
                # get x amount of characters from string that match the len of num starting from index
                substring = num_str[index:index + len(num)]
                # print(index, substring, num)
                if substring == num:
                    new_num_list.append(numbers[num])
    if len(new_num_list) == 0:
        continue
    elif len(new_num_list) == 1:
        calibration_values.append(new_num_list[0] + new_num_list[0])
        new_num_list.clear()
    else:
        calibration_values.append(new_num_list[0] + new_num_list[-1])
        new_num_list.clear()

for num in calibration_values:
    total += int(num)
print(total)
