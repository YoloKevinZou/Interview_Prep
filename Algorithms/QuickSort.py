import random

def quickSort(array):

	if len(array) <= 1:
		return array

	pivot = random.randint(0,len(array)-1)
	left = [x for x in array if x < array[pivot]]
	right = [x for i,x in enumerate(array) if x >= array[pivot] and i != pivot]

	return quickSort(left) + [array[pivot]]+ quickSort(right)


if __name__=="__main__":

	list1 = [5,4,9,13,1,6,8,7]
	list2 = []
	list3 = [5,3,4,8,9,2]
	list4 = [5,4,9,13,1,6,8,7,5]

	print(quickSort(list1))
	print(quickSort(list2))
	print(quickSort(list3))
	print(quickSort(list4))
