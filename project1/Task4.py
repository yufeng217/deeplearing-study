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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

""" 判断推销号码函数 """
def is_sell_phone(phone):
    """
        如果是推销，返回 [True, 电话]
        如果不是固话，返回 [False]
    """
    if phone[0:3] == "140":
        return [True, phone]
    else:
        return [False]
def sell_list():
    sell_list = []
    sell_called_list = []
    for phone in calls:
        sell_phone = is_sell_phone(phone[0])
        """ 是推销号码，且不再 list 中，则添加到推销号 list 中"""
        if sell_phone[0] and sell_phone[1] not in sell_list:
            sell_list.append(sell_phone[1])
        elif phone[1] in sell_list and phone[1] not in sell_called_list:
            """ 找出接收来电的推销号，添加到被叫 list 中"""
            sell_called_list.append(phone[1])
    """ 找出发送或接收短信的推销号，添加到被叫 list 中 """
    for phone in texts:
        if phone[0] in sell_list and phone[0] not in sell_called_list:
            sell_called_list.append(phone[0])
        if phone[1] in sell_list and phone[1] not in sell_called_list:
            sell_called_list.append(phone[1])
    """ 将被叫号 list 中的号在推销号 list 中删除 """
    return list(set(sell_list).difference(set(sell_called_list)))
    
    
_sell_list = sell_list()
_sell_list.sort()
_sell_list = "\n".join(_sell_list)
print("These numbers could be telemarketers:")
print(_sell_list)
