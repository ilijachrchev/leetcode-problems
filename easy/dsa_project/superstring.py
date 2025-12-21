def find_max_overlap(s1, s2):
    max_len = min(len(s1), len(s2))
    for length in range(max_len, 0, -1):
        if s1[-length:] == s2[:length]:
            return length
    return 0


n = int(input())
strings = []
for new in range(n):
    strings.append(input().strip())

overlap = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            overlap[i][j] = find_max_overlap(strings[i], strings[j])

superstring = strings[0]
last_idx = 0
used = [False] * n
used[0] = True

for i in range(n - 1):
    max_overlap = -1
    best_idx = -1

    for j in range(n):
        if not used[j]:
            if overlap[last_idx][j] > max_overlap:
                max_overlap = overlap[last_idx][j]
                best_idx = j

    superstring += strings[best_idx][max_overlap:]
    last_idx = best_idx
    used[best_idx] = True

print(superstring)