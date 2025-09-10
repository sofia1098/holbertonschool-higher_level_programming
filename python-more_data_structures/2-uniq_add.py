#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    nums = set(my_list)
    for i in nums:
        total += i
    return total
