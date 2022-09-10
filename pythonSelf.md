# Arrays

`* An array is a collection of items stored at contiguous memory locations.` 
* Store multiple items of the same data type together.
* Easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array.
    
```python
    import array
    
    #Creating: array(data_type, value_list)
    a = arr.array('i', [1, 2, 3])

    #Adding:
    a.insert(1, 4) # At any position
    a.append(5) # At end of array

    #Accessing: 
    a[3] # Access element at index 3

    #Traversing:
    def traverseArray(a): 
        for i in a:
            print(i)

    #Removing:
    a.pop(2) # Pop element at index 2
    a.remove(1) # Remove 1st occurrence of 1

    #Slicing:
    Sliced_array = a[3:8] # Range slicing    
        
    Sliced_array = a[5:] # Pre-defined point to end    
        
    Sliced_array = a[:] # Beginning till end

    #Searching:
    a.index(2) # Index of 1st occurrence of 2

    #Updating:
    arr[2] = 6 # Updating a element in a array
            
```
Complexity:

|Operation|Time|Space|
|---|---|---|
|Creating|O(1)|O(N)|
|Adding|O(1)/O(N)|O(1)|
|Accessing|O(1)|O(1)|
|Traversing|O(N)|O(1)|
|Removing|O(1)/O(N)|O(1)|
|Slicing|O(N)|O(1)|
|Searching|O(N)|O(1)|
|Updating||O(1)|


# Sorting

Defn:   To sort the elements in a particular order. aesc or desc.

Insertion Sort:        
    ` The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.`

    Complexity:
        Time O(n^2)
        Space O(1)
    -Stable
    -Sorting In Place
    -Online
    -Best case: Array is already sorted. 
    -Worst case: Array is reverse sorted.

Buble Sort:     
    `Repeatedly swapping the adjacent elements if they are in wrong order.`

    Complexity:
        Time O(n^2)
        Space O(1)
    -Stable
    -Sorting In Place
    -Online
    -Best case: Array is already sorted. 
    -Worst case: Array is reverse sorted. .

    Optimization:
        Adding flag such that if it's value is set to False then no swapping is required.
    
Selection Sort:     
    `Segment the input array into two list i.e sorted and unsorted. Continuously remove the smallest element of the unsorted segment of the list and append it to the sorted segment.`

    Complexity:
        Time O(n^2)
        Space O(1)
    -Not Stable
    -Sorting In Place
    -Offline
    -Best, average and worst case: Independent of distribution of data.    

Heap Sort:     
    `Segment the input array into two list i.e sorted and unsorted. Convert unsorted segment into Heap data structure, so that we can efficiently determine the largest element`

    Complexity:
        Time O(nlogn)
        Space O(1)
    -Not Stable
    -Sorting In Place
    -Offline
    -Best, average and worst case: Independent of distribution of data. 

# Searching

Defn:   Used to look for presence of a particular item in a DS.

Linear Search (Sequential Search):
    -   One-by-One search.
    -   Good choice when unsorted array.
    
    Time Complexity O(N)
    Space Complexity O(1)    

Binary Search:
    -   Faster than Linear Search.
    -   Half of remaining element can be eliminated at a time, instead of one by one.
    -   Works only for sorted arrays.

    Time Complexity O(logN) eg: Log2(32) = 5 #32 elements worst case will take 5 steps.
    Space Complexity O(1)

#>
