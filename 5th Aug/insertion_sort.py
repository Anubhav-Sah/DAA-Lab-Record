def insertion_sort(arr, n):
    # Base case
    if n <= 1:
        return
    
    # Sort first n-1 elements
    insertion_sort(arr, n - 1)
    
    # Insert nth element into sorted array
    last = arr[n - 1]
    j = n - 2
    
    # Move elements greater than last up one position
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last
arr = [5, 3, 4, 1]
insertion_sort(arr, len(arr))
print(arr)  # Output: [1, 3, 4, 5]
