import unittest

def lcs(sequence1, sequence2):
	map1 = dict()
	for index, item in enumerate(sequence1):
		if item not in map1:
			map1[item] = set()		
		map1[item].add(index)
	
	result = []
	tmp = []
	tmp_prev_indexs = None
	for index, item in enumerate(sequence2):
		if item not in map1:
			
			if len(tmp) > 0:
				if len(result) < len(tmp):
					result = tmp
				tmp = []
				tmp_prev_indexs = None
			
			continue
		
		if len(tmp) > 0:
			item_indexs = map1[item]
			new_tmp_prev_indexs = set()
			for item_index in item_indexs:
				if tmp_prev_indexs and (item_index-1) in tmp_prev_indexs:
					new_tmp_prev_indexs.add(item_index)
			
			if new_tmp_prev_indexs:
				# looks good, continue adding previous subsequence
				tmp.append(item)
				tmp_prev_indexs = new_tmp_prev_indexs;
			else:
				# this item not ok, the previous subsequence will break now to start a new one
				if len(result) < len(tmp):
					result = tmp
				tmp = [item]
				tmp_prev_indexs = map1[item]

		else:
			tmp.append(item)
			tmp_prev_indexs = map1[item]

		if (index+1) == len(sequence2):
			if len(result) < len(tmp):
				result = tmp


	return result

class TestLCS(unittest.TestCase):

	def test_lcs(self):
		sequence1 = [1, 2, 3, 4, 5, 8, 9, 10]
		sequence2 = [6, 3, 4, 5, 8, 2, 3, 4]
		result = lcs(sequence1, sequence2)
		self.assertListEqual(result, [3, 4, 5, 8])


		sequence1 = [1, 2, 3, 4, 5, 8, 9, 10]
		sequence2 = [6, 3, 4, 5, 8, 2, 3, 4, 5]
		result = lcs(sequence1, sequence2)
		self.assertListEqual(result, [3, 4, 5, 8])


		sequence1 = [1, 2, 3, 4, 5, 8, 9, 10]
		sequence2 = [6, 3, 4, 5, 8, 2, 3, 4, 5, 8]
		result = lcs(sequence1, sequence2)
		self.assertListEqual(result, [2, 3, 4, 5, 8])

		sequence1 = [1, 2, 3, 4, 5, 8, 9, 10]
		sequence2 = [6, 2, 3, 4, 6, 4, 5, 8, 9, 3, 4]
		result = lcs(sequence1, sequence2)
		self.assertListEqual(result, [4, 5, 8, 9])

		sequence1 = ['A', 'B', 'A', 'B', 'C']
		sequence2 = ['B', 'A', 'B', 'C', 'A']
		result = lcs(sequence1, sequence2)
		self.assertListEqual(result, ['B', 'A', 'B', 'C'])

unittest.main()
