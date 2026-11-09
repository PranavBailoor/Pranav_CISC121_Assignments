def solution(A):
    if len(A) == 0:#if the array is empty, return 0
        return 0
    result = 0
    for number in A:
        result ^= number #XOR operation to find the number that occurs an odd number of times
    return result

A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))