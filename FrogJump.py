import math

def solution(X,Y,D):
    if X == Y: #if no distance to cover, return 0
        return 0
    jumps = math.ceil((Y - X) / D) #calculate the number of jumps needed to cover the distance(x-y)
    return jumps

X = 10
Y = 85
D = 30
print(solution(X,Y,D))