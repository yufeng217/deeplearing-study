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
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

""" 判断固话函数 """
def is_fixed_telephone(phone):
    """
        如果是固话，返回 [True, 区号, 电话]
        如果不是固话，返回 [False]
    """
    rightIndex = phone.find(")")
    if phone[0:2] == "(0" and rightIndex > 0:
        return [True, phone[1:int(rightIndex)], phone[int(rightIndex + 1): -1]]
    else:
        return [False]

""" 判断是否是班加罗尔固定电话 """
def is_bangalore_fixed_telephone(phone):
    fixed_telephone = is_fixed_telephone(phone)
    if fixed_telephone[0] and fixed_telephone[1] == "080":
        return fixed_telephone
    else:
        return [False]

""" 判断移动电话函数 """
def is_mobile_phone(phone):
    """
        如果是移动电话，返回 [True, 前缀, 电话]
        如果不是固话，返回 [False] 
    """
    if phone[0] in ['7', '8', '9'] and " " in phone:
        return [True, phone[0:4], phone]
    else:
        return [False]

""" 遍历通话记录，找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号），去重存到列表 """
def bangalore_codes():
    codes = {}
    
    for item in calls:
        bangalore_fixed_telephone = is_bangalore_fixed_telephone(item[0])
        if bangalore_fixed_telephone[0]:
            
            fixed_telephone = is_fixed_telephone(item[1])
            if fixed_telephone[0] and fixed_telephone[1] not in codes:
                codes[fixed_telephone[1]] = 1
            elif fixed_telephone[0] and fixed_telephone[1] in codes:
                codes[fixed_telephone[1]] += 1
                
            mobile_telephone = is_mobile_phone(item[1])
            if mobile_telephone[0] and mobile_telephone[1] not in codes:
                codes[mobile_telephone[1]] = 1
            elif mobile_telephone[0] and mobile_telephone[1] in codes:
                codes[mobile_telephone[1]] += 1

    return codes

""" 排序，给每个区号后增加换行符，输出 """
def part_one(bangalore_code_list):
    bangalore_code_list.sort()
    bangalore_code_list = "\n".join(bangalore_code_list)
    print("The numbers called by people in Bangalore have codes:")
    print(bangalore_code_list)
    
# 测试用例
#print(is_fixed_telephone("(080)45291968"))
#print(is_bangalore_fixed_telephone("(080)45291968"))
#print(is_mobile_phone("90365 06212"))

def part_two(bangalore_codes):
    sum_value = sum(bangalore_codes.values())
    bangalore_value = bangalore_codes["080"]
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(format(bangalore_value / sum_value * 100, '.2f')))
_bangalore_codes = bangalore_codes()
_bangalore_code_list = list(_bangalore_codes.keys())

part_one(_bangalore_code_list)
part_two(_bangalore_codes)
