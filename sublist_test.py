test_case = """9 6 6 9 9 9
3
3
10
"""
# test_case = """5 10 15 20 25
# 3
# 5
# 11
# """
# list
# limit
# divisor
# result

#Plan
"""
First I am going to create all possible sublist with the determined limit
from that I am going to check if that list can be divided by the divisor if it is I will 
check if it already exist in a big list of sublist, and if it does not I will add it
and in the end I will count the ammount of list on that list of sublist
"""

new_test_case = test_case.split("\n")

sub_list_group = []

def check_sub_list_existence(_list: list[int], divisor: int):
    """
    Here I chechk if a list is valid to be added to a list of subList
    """
    for item in _list:
        if item % divisor != 0:
            return
    if _list in sub_list_group:
        return
    sub_list_group.append(_list.copy())


def sub_list_builder(_list: list[int], limit: int, divisor: int):
    """
    here I look if a sublist have more sublist inside
    """
    check_sub_list_existence(_list, divisor)
    _list.pop()
    if len(_list) != 0:
        return sub_list_builder(_list, limit, divisor)
    else:
        return

def sub_list_searcher(_list: list[int], limit: int, divisor: int):
    """
    Here I set up all the possible sublist with the length of the limit or less depending if we reach the
    end of the list
    """
    cent = 0
    while cent < len(_list):
        local_limit = cent+limit
        local_limit = local_limit if local_limit < len(_list) else len(_list)

        sub_list_builder(_list[cent:local_limit], cent, divisor)
        cent += 1
    return len(sub_list_group)

def check_test_case():
    """
    Here I prepare the test case to be use and execute the needed code
    """
    value = sub_list_searcher(
        [int(item) for item in new_test_case[0].split(" ")], 
        int(new_test_case[1]),
        int(new_test_case[2]))
    print(value)
    if value == int(new_test_case[3]):
        return True
    return False

print(check_test_case())
