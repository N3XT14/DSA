#Efficient Algorithm for finding the subarray in a 1-D Array with maximum sum.

#Basic Idea: Use max value calculated in lower size subarray and update the max accordingly which can be used as standard comparison parameter.
#Eg. [-2, 1, -3, 4, -1, 2]
#compare([-2,1]) ans = 1(max)
#compare([ans + (-3),-3]) ans = -2(max)
#compare([ans + (4),4]) ans = 4(max)
#compare([ans + (-1),-1]) ans = 3(max)
#compare([ans + (2), 2]) ans = 5(max)

#Kaden's Algorithm Basic Approach(with start and end indices of the subarray).
from sys import maxsize
def maxSubArraySum(a,size):     
	max_so_far = -maxsize - 1
	max_ending_here = 0
	start,end,s = 0,0,0
 
	for i in range(0, size):
		max_ending_here += a[i]
		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1
	return max_so_far
a = [-2, 1, -3, 4, -1, 2]
print(maxSubArraySum(a, len(a)))


#Applying Kaden's algorithm to get maxium subMatrix of dim RxC

def kadanes(arr, n):
	s, maxi = arr[0], arr[0]
	for i in range(1,n):
		s += arr[i]
		s = max(s,arr[i])
		maxi = max(s,maxi)
	return maxi
	
	
def maximumSumRectangle(R,C,M):	
	res = M[0][0]
	for starti in range(R):
		subMatSum = [0 for _ in range(C)]
		for i in range(starti, R):
			for j in range(C):
				subMatSum[j] += M[i][j]
			print(subMatSum)
			res = max(res, kadanes(subMatSum, C))
			print(res)
	return res

R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
# maximumSumRectangle(R,C,M)