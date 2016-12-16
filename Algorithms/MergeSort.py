def split(array):
	
	if len(array) <= 1:
		return array
	
	mid = len(array) / 2
	firstHalf = array[:mid]
	secondHalf = array[mid:]

	leftSorted = split(firstHalf)
	rightSorted = split(secondHalf)
	return merge(leftSorted, rightSorted)


def merge(left, right):

	if not left or not right:
		return left + right

	else:
		if left[0] < right[0]:
			return [left[0]] + merge(left[1:], right)
		else:
			return [right[0]] + merge(left, right[1:])


if __name__=="__main__":

	list1 = [5,4,9,13,1,6,8,7]
	list2 = []
	list3 = [5,3,4,8,9,2]
	list4 = [5,4,9,13,1,6,8,7,5]

	print(split(list1))
	print(split(list2))
	print(split(list3))
	print(split(list4))