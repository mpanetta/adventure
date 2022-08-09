def quick_sort(array):
    length = len(array)
    if(length <= 1): return array

    pivot = array.pop()
    left = []
    right = []

    for i in range(0, length -1):
        elem = array[i]

        if(elem <= pivot): left.append(elem)
        if(elem > pivot): right.append(elem)
    return [*(quick_sort(left)), pivot, *(quick_sort(right))] 

def quick_sort_in_place(array, start=0, end=None):
    print(f"array: {array}, start: {start}, end: {end}")
    pivot = start
    if(end == None): end = len(array) - 1
    print(array[pivot])

    for i in range(start, end):
        print(f"arraydfds {array}, pivot: {array[pivot]}")

        if(array[i] <= array[pivot]):
            array[i], array[pivot] = array[pivot], array[i]
            pivot += 1
        
    return array
