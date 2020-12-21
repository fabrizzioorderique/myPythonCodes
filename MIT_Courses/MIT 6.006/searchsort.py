# Common searching and sorting algorithms
# Written by Piero Orderique
# Date Started: 12/21/2020

####################################################
############          SEARCHES          ############
####################################################
def binarysearch(target: object, arr: list) -> bool:
    """input a list and return True if target in arr. Assumes arr is sorted ascending. 
    O(lgn) time, O(1) space?
    >>> binarysearch(10, [])
    False
    >>> binarysearch(3, [1,2,3])
    True
    >>> binarysearch(3, [2])
    False
    """
    # if empty, return false
    if arr == []: return False
    # else look in middle array
    mid = len(arr)//2
    if target == arr[mid]: return True
    # if target is less, look in left half
    elif target < arr[mid]: return binarysearch(target, arr[0:mid])
    # else, let's check in right half
    else: return binarysearch(target, arr[mid+1:]) # could produce out of bounds error

###################################################
############           SORTS           ############
###################################################
def insertionsort(arr: list) -> None:
    """returns original list but sorted. 
    O(n^2) time, O(1) space
    >>> insertionsort([])
    []
    """
    # if empty, just go ahead and return empty list
    if arr == []: return arr
    # else, we iterate through elems of the list - for every element, 
    for idx in range(1, len(arr)):
        # insert it in our sorted array by swapping until no more swaps needed, going backwards
        for idx2 in range(idx-1, -1, -1):
            if arr[idx] < arr[idx2]: 
                # swap if greater and continue
                arr[idx], arr[idx2] = arr[idx2], arr[idx]
                continue
            # if its greater or equal to previous, then leave it there
            else: break
               
               

    

if __name__ == "__main__":
    import doctest
    doctest.testmod()