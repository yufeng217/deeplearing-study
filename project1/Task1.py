"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

""" 遍历给定列表，将索引 0 和 1 的电话与给定列表对比去重，返回新列表 """
def remove_duplicates(duplicates_list, phone_list):
    for record in duplicates_list:
        if record[0] not in phone_list:
            phone_list.append(record[0])

        if record[1] not in phone_list:
            phone_list.append(record[1])
            
    return phone_list


_phone_list = []

_phone_list = remove_duplicates(texts, _phone_list)
_phone_list = remove_duplicates(calls, _phone_list)

print("There are {} different telephone numbers in the records.".format(len(_phone_list)))
