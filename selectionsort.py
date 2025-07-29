
import time

def selection_sort(arr):
# Sort the element using selection sort
# Input-> n number of element
# Output-> sorted array

    for i in range(len(arr)):
        smallest_index= i
        for j in range(1,len(arr)):
            if arr[j]<arr[smallest_index]:
                smallest_index=j
        arr[i],arr[smallest_index]=arr[smallest_index],arr[i]
    return arr


def main():
    arr=input("Enter the elements of the array using space : ").split()
    
    arr=[int(i) for i in arr]
    start_time=time.time()
    sorted_array=selection_sort(arr)
    end_time=time.time()
    print(f"Sorted array : {sorted_array}")
    print(f"Total time taken : {end_time-start_time}")


main()
















