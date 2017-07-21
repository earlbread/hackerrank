def solution(A):
    if len(A) < 2:
        return 0
    split_index = -1
    score = 0
    left = 0

    right = sum(A)
    for i in range(len(A)):
        left += A[i]
        right -= A[i]

        if left == right:
            split_index = i + 1
            score += 1
            break

    if split_index != -1:
        score += max(solution(A[:split_index]), solution(A[split_index:]))
    return score

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split(" ")))
    print(solution(A))
