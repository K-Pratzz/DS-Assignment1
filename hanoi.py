def hanoi(n,source,auxillary,target,count=0):
    if n==1:
        print("move disk 1 from source",source,"to target",target)
        return 1
    
    count=hanoi(n-1,source,auxillary,target,count)
    print("move disk",n,"from source",source,"to target",target)
    count+=1
    count=hanoi(n-1,auxillary,target,source,count)
    return count

print(hanoi(3,'A','B','C'))
#time complexity is O(2**n -1) and space O(n) 
'''
Aim: To generate a step-by-step solution and observe exponential growth.
Move Sequence for N=3 (Source: A, Aux: B, Dest: C):
​Move Disk 1 from A to C
​Move Disk 2 from A to B
​Move Disk 1 from C to B
​Move Disk 3 from A to C
​Move Disk 1 from B to A
​Move Disk 2 from B to C
​Move Disk 1 from A to C
​Complexity Statement:
​Move Count for N=4: 2^4 - 1 = 15 moves.
​Time Complexity: O(2^n) because every additional disk doubles the required moves.

'''