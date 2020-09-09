import unittest
import random
import time

def merge2list(list1, list2):
    result_left = []
    result_right = []

    cal_stack = [list1, list2]
    while len(cal_stack) > 0:
        sublist1 = cal_stack.pop()
        sublist2 = cal_stack.pop()

        if len(sublist1) == 0:
            result_left.extend(sublist2)
        elif len(sublist2) == 0:
            result_left.extend(sublist1)
        else:
            # left list
            left_list = None
            left_barier = None
            if sublist1[0] != sublist2[0]:
                left_list = sublist1 if sublist1[0] < sublist2[0] else sublist2
                left_barier = sublist2[0] if sublist1[0] < sublist2[0] else sublist1[0]

            # right list
            right_list = None
            right_barier = None
            if sublist1[-1] != sublist2[-1]:
                right_list = sublist2 if sublist1[-1] < sublist2[-1] else sublist1
                right_barier = sublist1[-1] if sublist1[-1] < sublist2[-1] else sublist2[-1]

            if left_list:
                while len(left_list) > 0:
                    n = left_list[0]
                    if n > left_barier:
                        break
                    else:
                        left_list.pop(0)
                        result_left.append(n)

            if right_list:
                while len(right_list) > 0:
                    n = right_list[-1]
                    if n < right_barier:
                        break
                    else:
                        right_list.pop()
                        result_right.insert(0, n)

            if not left_list and not right_list:
                if len(sublist1):
                    result_left.append(sublist1.pop(0))
                if len(sublist2):
                    result_left.append(sublist2.pop(0))
                if len(sublist1):
                    result_right.insert(0, sublist1.pop())
                if len(sublist2):
                    result_right.insert(0, sublist2.pop())

            cal_stack.append(sublist1)
            cal_stack.append(sublist2)
        

    return result_left + result_right

def normal_sort(list1, list2):
    result = list1 + list2
    l = len(result)
    for i, n in enumerate(result):
        for j in range(i+1, l):
            if result[i] > result[j]:
                tmp = result[i]
                result[i] = result[j]
                result[j] = tmp

    return result

class Test(unittest.TestCase):
    def test_merge2list(self):
        num = 3000
        for i in range(20):
            print("----------- round " + str(i+1) + " -----------")
            list1 = [random.randint(1, 1999) for iter in range(num)]
            list1.sort()
            list2 = [random.randint(1, 1999) for iter in range(num)]
            list2.sort()
            list3 = [n for n in list1]
            list4 = [n for n in list2]
            
            start_time = int(round(time.time() * 1000))
            expected = list1 + list2
            expected.sort()
            end_time = int(round(time.time() * 1000))
            print("python sort complete at: " + str(end_time - start_time))

            start_time = int(round(time.time() * 1000))
            merged = merge2list(list1, list2)
            end_time = int(round(time.time() * 1000))
            print("merge sort complete at: " + str(end_time - start_time))
            self.assertListEqual(merged, expected)

            start_time = int(round(time.time() * 1000))
            merged = normal_sort(list3, list4)
            end_time = int(round(time.time() * 1000))
            print("normal sort complete at: " + str(end_time - start_time))
            self.assertListEqual(merged, expected)

unittest.main()