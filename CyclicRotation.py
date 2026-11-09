def solution(A, K):
    B = [None] * len(A) #create new array with the same length as A
    for i in range(len(A)):
        B[i] = A[i - K] #copy the elements from A to B, shifted by K positions to the right
    return B

A = [3, 8, 9, 7, 6]
print(solution(A, 3))