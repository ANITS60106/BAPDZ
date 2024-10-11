def tsepytuponaiti(h, k):
    count = 1
    for i in range(len(h) - 1):
        if abs(h[i] - h[i + 1]) > k:
            count += 1
    return count

def k_tasamayaraznitsaprokotoruyugovorilRuslan(n, m, h):
    low = 0
    rostiks = 1000000
    out = -1

    while low <= rostiks:
        mid = (low + rostiks) // 2
        с = tsepytuponaiti(h, mid)

        if с == m:
            out = mid
            rostiks = mid - 1
        elif с < m:
            rostiks = mid - 1
        else:
            low = mid + 1

    return out

n, m = input().split()
n, m = int(n), int(m)
h = [int(x) for x in input().split()]

out = k_tasamayaraznitsaprokotoruyugovorilRuslan(n, m, h)

print(out)
