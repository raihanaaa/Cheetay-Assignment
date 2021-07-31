def longestPalin(S):
    if len(S) <= 1: return S
    max_len = 1
    n = len(S)
    st, end = 0, 0
    # Even length
    for i in range(n - 1):
        l, r = i, i + 1
        while l >= 0 and r < n:
            if S[l] == S[r]:
                l, r = l - 1, r + 1
            else:
                break
        palin_len = r - l - 1
        if palin_len > max_len:
            max_len = palin_len
            st, end = l + 1, r - 1

    # Odd length
    for i in range(n - 1):
        l, r = i, i
        while l >= 0 and r < n:
            if S[l] == S[r]:
                l, r = l - 1, r + 1
            else:
                break
        palin_len = r - l - 1
        if palin_len > max_len:
            max_len = palin_len
            st, end = l + 1, r - 1

    return S[st:end + 1]


print(longestPalin("abacada"))
