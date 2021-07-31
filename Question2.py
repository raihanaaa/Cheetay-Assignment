from itertools import permutations
def printLargest(arr):
    l = [x for x in permutations(arr)]
    s = []
    for i in l:
        s.append(''.join(str(x) for x in i))
    return max(s)

print(printLargest([54, 546, 548, 60]))