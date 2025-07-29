import time

def binary(arr,target,low,high):
    if low>high:
        return -1

    mid=(low+high)//2

    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary(arr,target,mid+1,high)
    else:
        return binary(arr,target,low,mid-1)
     
def _main_():
    arr=input("Enter the value of array using space : ").split()
    arr=[int(x)for x in arr]

    high=int(len(arr))

    low=0

    target=int(input("Enter the value to be search : "))

    strt=time.time()

    index=binary(arr,target,low,high)

    endt=time.time()


    if index != -1:
        print(f"{target} is found at index {index}")
    else:
        print(f"{target} is not found in the array")

    print(f"Time taken by binary search: {endt - strt:.6f} sec")


_main_()