from merge2list import merge2list
import random
import unittest

def mergesort(items):
    if len(items) < 2:
        return items

    if len(items) == 2:
        if items[0] > items[1]:
            tmp = items[0]
            items[0] = items[1]
            items[1] = tmp
        return items

    cal_stack = []
    result = []

    break_index = int(len(items) / 2)
    list1 = items[0:break_index]
    list2 = items[break_index:]

    list1 = mergesort(list1)
    list2 = mergesort(list2)

    result = merge2list(list1, list2)
    return result

class Test(unittest.TestCase):
    def test_mergesort(self):
        num = 20000
        items = [random.randint(1, 1999) for iter in range(num)]
        items2 = [n for n in items]

        items2.sort()
        items = mergesort(items)
        self.assertListEqual(items, items2)

if __name__ == '__main__':
    unittest.main()
    