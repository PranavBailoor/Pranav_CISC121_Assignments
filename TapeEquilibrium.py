def solution(A):
    result = max(A)#initialize result to the maximum value in the array
    for i in range(len(A)-1):
        sum1, sum2 = 0, 0#initialize sum1 and sum2 to 0
        for j in range(0, i):
            sum1 += A[j]#sum the first part of the array
        for k in range(i, len(A)):
            sum2 += A[k]#sum the second part of the array
        if abs(sum1 - sum2) < result:
            result = abs(sum1 - sum2)# find lowest difference and return it
    return result

A = [3, 1, 2, 4, 3]
print(solution(A))