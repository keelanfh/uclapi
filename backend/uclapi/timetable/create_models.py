file_string = open("Full_DDL.sql").read()
# file_string = open("test.txt").read()


def find_all(word, string):
    index_starts = []
    stripped_length = 0
    while string.find(word) != -1:
        index_starts.append(stripped_length + string.find(word))
        string = string[string.find(word) + 12:]
        stripped_length += (index_starts[-1] + 12)
    return index_starts


data = {}

for index in find_all("CREATE TABLE", file_string):
    start = index
    while file_string[index] != "(":
        index += 1
    table_name = file_string[start: index]

    counter = 1
    start = index
    index += 1
    while counter and index < len(file_string):
        if file_string[index] == "(":
            counter += 1
        elif file_string[index] == ")":
            counter -= 1
        index += 1
    table_fields = file_string[start + 1: index - 1].split("\n")
    data[table_name] = table_fields


# array = list(filter(lambda k: k[:12] == "CREATE TABLE", data.keys()))
# print(array)
# # print(len(data.keys()))
# #
import json
#
# for index in find_all("CREATE TABLE", file_string):
#     print(index)
#     print(file_string[index: index + 12])

print(json.dumps(data, indent=4))
