'''
Aim: To implement binary search and understand logarithmic recurrence.
Recurrence Intuition:
The problem size is halved at each step: T(n) = T(n/2) + O(1).
This results in a Time Complexity of O(\log n).
​Implementation Checkpoints:
​Mid-logic: mid = (low + high) // 2.
​Termination: Returns -1 if low > high (key not found or empty list).
​Requirement: Data must be sorted for the halving logic to be valid.

'''

def binary(arr,target,low,high):
    if low > high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary(arr,target,low,mid-1)
    else:
        return binary(arr,target,mid+1,high)
arr=[10,20,30,40,50]
target=30
print(binary(arr,target,0,len(arr)-1))