
def getMaxAdditionalDinersCount(N, K, M, S) -> int:
    S = sorted(S)
    total = 0

    total += (S[0]-1)//(K+1)
    total += (N - S[-1])//(K+1)

    for i in range(M-1):
        distance = S[i+1] - S[i] - 1
        total += max((distance - K)//(K+1), 0)
    return total 

N = 10
K = 1
M = 2
S = [2, 6]

print(getMaxAdditionalDinersCount(N, K, M, S))