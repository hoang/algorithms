import unittest

def lcs(sequence1, sequence2):
	map1 = dict()
	
	# iterate sequence1
	for index, item in enumerate(sequence1):
		if item not in map1:
			map1[item] = set()		
		map1[item].add(index)
	
	result = []
	tmp = []
	tmp_prev_indexs = None
	pointer_index = 0

	def set_result_if_need(reset_tmp = False):
		nonlocal result, tmp, tmp_prev_indexs
		if len(result) < len(tmp):
			result = tmp
		if reset_tmp:
			tmp = []
			tmp_prev_indexs = None


	# iterate sequence2 by increasing pointer_index along with process
	while pointer_index < len(sequence2):

		next_pointer_index = pointer_index

		for index in range(pointer_index, len(sequence2)):		
			item = sequence2[index]

			if item not in map1:
				if len(tmp) > 0:
					set_result_if_need(True)	
				continue
			
			# item existed in map1
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
					# this item not ok, we will start a new round of pointer_index
					set_result_if_need(True)
					break

			else:
				tmp.append(item)
				tmp_prev_indexs = map1[item]
				next_pointer_index = index + 1

			if (index+1) == len(sequence2):
				set_result_if_need()

		if next_pointer_index > pointer_index:
			pointer_index = next_pointer_index # then start new round with new pointer_index
		else:
			break

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

		sequence1 = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'd', 'd']
		sequence2 = ['a', 'b', 'c', 'd', 'd']
		result = lcs(sequence1, sequence2)
		self.assertListEqual(result, ['b', 'c', 'd', 'd'])

unittest.main()
