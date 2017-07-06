n, k = list(map(int, input().split()))
array = list(map(int, input().split()))

pos = {}
for i in range(n):
    pos[array[i]] = i

for i in range(n):
    if k == 0:
        break

    if array[i] == (n - i):
        continue

    maxIndex = pos[n - i]
    pos[array[i]] = pos[n - i]
    pos[n - i] = i

    array[i], array[maxIndex] = array[maxIndex], array[i]
    k -= 1

print(" ".join(map(str, array)))
