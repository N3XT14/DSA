def insertionSort(arr):

    for i in range(1, len(arr)):
        item_to_insert = arr[i]

        j = i-1
        while ( j>=0 and item_to_insert < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = item_to_insert
    
    return arr

def bubleSort(arr):
    
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

    return arr

def selectionSort(arr):

    for idx, ele in enumerate(arr):
        lowest_value_index = idx

        for j in range(idx+1,len(arr)):
            if arr[j] < ele:
                lowest_value_index = j
        
        arr[idx], arr[lowest_value_index] = arr[lowest_value_index], arr[idx]

    return arr

# def heapSort(arr):
    
def cycleSort(nums):

    for i,ele in enumerate(nums):
        while 0<= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tp = nums[i] - 1
            nums[i],nums[tp] = nums[tp],nums[i]  
    return nums
arr = [64, 34, 25, 12, 22, 11, 90]

# print(insertionSort(arr))
# print(bubleSort(arr))
# print(selectionSort(arr))
# print(cycleSort([-1,5,6,2,3,4,1]))