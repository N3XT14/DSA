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

		mid = (high + low) // 2

		if arr[mid] < x:
			low = mid + 1
		elif arr[mid] > x:
			high = mid - 1		
		else:
			return mid	
	return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10
#print(binary_search(arr, x))

def reverse1(x):
	if x in range(-9,10):
		return x
	limit = 2**31        
	l = list(str(x))
	l.reverse()
	if x < 0:
		l = l[:-1]
	rev = ''.join(l)        
	
	rev = int(rev)
	
	
	if -limit <= rev <= ( limit - 1):
		if x < 0:
			return -rev
		return rev
	return 0

print(reverse1(9))