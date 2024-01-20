def getMaxDinersCount(N,K,M,S):
    S.sort()
    additional_diners = 0
    prev_seat = S[0]
    
    for current_seat in S[1:]:
        gap = current_seat - prev_seat - 1
        additional_diners += max(0,(gap-K)//(K+1))
        prev_seat = current_seat

    front = S[0] - 1 + K
    tail = N - S[-1] + K
    additional_diners += max(0,(front-K)//(K+1))
    additional_diners += max(0,(tail-K)//(K+1))
    return additional_diners
