def linearearch(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

#print(linearearch([8,7,6,5], 6))


def binary_search(arr, x):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:

		mid = low + ((high - low) // 2) # To avoid integer overflow

		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1		
		else:
			return mid	
	return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
# print(binary_search(arr, x))

def binary_search_variation1(arr,x):
	low = 0
	high = len(arr) - 1
	mid = 0
	ans = -1

	while low <= high:

		mid = low + ((high - low) // 2) # To avoid integer overflow

		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1		
		elif arr[mid] == x:
			ans = mid
			high = mid - 1	# To find first occurence
			# low = mid + 1 	# To find last occurence
	return ans

arr = [ 2, 3, 3, 4, 10, 10, 40 ]
x = 3
# print(binary_search_variation1(arr, x))

# Find index of first occurrence of least element
# greater than key in array i.e upper_bound
def binary_search_variation2(arr,x):
	low = 0
	high = len(arr) - 1
	mid = 0
	ans = -1

	while low <= high:

		mid = low + ((high - low + 1) // 2) # To avoid integer overflow

		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			ans = mid
			high = mid - 1		
		elif arr[mid] == x:
			low = mid + 1 	
	return ans

arr = [ 2, 3, 3, 4, 10, 10, 40 ]
x = 3
print(binary_search_variation2(arr, x))


# Find index of last occurrence of greatest element
# less than key in array
def binary_search_variation3(arr,x):
	low = 0
	high = len(arr) - 1
	mid = 0
	ans = -1

	while low <= high:

		mid = low + ((high - low + 1) // 2) # To avoid integer overflow

		if arr[mid] < x:
			ans = mid
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1		
		elif arr[mid] == x:
			high = mid - 1 	
	return ans

arr = [ 2, 3, 3, 4, 10, 10, 40 ]
x = 3
print(binary_search_variation3(arr, x))