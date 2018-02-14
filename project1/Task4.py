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

def remove_duplicate(list):
    ret_list = []
    for element in list:
        if element not in ret_list:
            ret_list.append(element)
    return ret_list

def sell_list(call_phone_list):

    """ 被叫号码如果在主叫号 list 中，证明该号不是推销号，从主叫号 list 中删除 """
    for phone in calls:
        if phone[1] in call_phone_list:
            call_phone_list.remove(phone[1])
        
    """ 发送短信号或接收短信号如果在主叫号 list 中，证明该号不是推销号，从主叫号 list 中删除 """
    for phone in texts:
        if phone[0] in call_phone_list:
            call_phone_list.remove(phone[0])
        if phone[1] in call_phone_list:
            call_phone_list.remove(phone[1])
    
    return call_phone_list
    
_call_phone_list = remove_duplicate([call[0] for call in calls])

_sell_list = sell_list(_call_phone_list)
_sell_list.sort()
_sell_list = "\n".join(_sell_list)
print("These numbers could be telemarketers:")
print(_sell_list)
