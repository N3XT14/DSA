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

Definition:   To sort the elements in a particular order. aesc or desc.

[Code Link](https://github.com/N3XT14/DSA/blob/main/Algorithms/Sorting/Sorting.py)

Insertion Sort:        
    `The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.`

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

Definition:   Used to look for presence of a particular item in a DS.

[Code Link](https://github.com/N3XT14/DSA/blob/main/Algorithms/Searching/Searching.py)

Linear Search (Sequential Search):

    -   One-by-One search.
    -   Good choice when unsorted array.
    
    Time Complexity O(N)
    Space Complexity O(1)    

Binary Search:

    -   Faster than Linear Search.
    -   Half of remaining element can be eliminated at a time, instead of one by one.
    -   Works only for sorted arrays.

    Time Complexity O(logN) + 1 => O(logN)  eg: Log2(32) = 5 #32 elements worst case will take 5 steps + 1(last value in worst case).
    Space Complexity O(1)

    # Variations

    1. Contains: Nomral Binary Search
    2. Lower_Bound(First Occurence): bisect.bisect_left(a, x, lo=0, hi=len(a))
    3. Last Occurence: Same as Lower bound with updating the high value.
    4. Upper_Bound: bisect.bisect_right(a, x, lo=0, hi=len(a))
    Index of first occurrence of least element greater than key in array.
    5. Index of last occurrence of greatest element less than key in array.
#>


# Game Theory

1.  Game of Nim:

    PS: 

        Given a number of piles in which each pile contains some numbers of stones/coins. In each turn, a player can choose only one pile and remove any number of stones (at least one) from that pile. The player who cannot move is considered to lose the game (i.e., one who take the last stone is the winner). 

    Stratergy:
        
        Factors:
            -   The player who starts first.
            -   The initial configuration of the piles/heaps.

        If both A and B play optimally (i.e- they don’t make any mistakes), then the player starting first is guaranteed to win if the Nim-Sum at the beginning of the game is non-zero. Otherwise, if the Nim-Sum evaluates to zero, then player A will lose definitely.
        Nim-Sum:  Cumulative XOR value of the number of coins/stones in each piles/heaps at any point of the game.