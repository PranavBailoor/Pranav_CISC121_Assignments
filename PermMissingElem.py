def solution(A):
    if len(A) == 0:#if the array is empty, return 1
        return 1
    for i in range(1, len(A)+1):
        if (i in A) != True:#if the number doesn't match one in the array, return that number
            return i

A = [2, 3, 1, 5]
print(solution(A))