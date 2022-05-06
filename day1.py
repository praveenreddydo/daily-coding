"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."""


def sum_of_two(list,k):
    total = set()
    for i in list:
        if k - i in total:
            return True
        total.add(i)
    return False
    

list=[10,15,3,7]
k=17
print(sum_of_two(list,k))