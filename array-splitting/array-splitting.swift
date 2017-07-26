import Foundation

func solution(_ A: [Int]) -> Int {
    if A.count < 2 {
        return 0
    }

    var splitIndex = -1
    var score = 0
    var left = 0
    var right = A.reduce(0, +)

    for i in 0..<A.count {
        left += A[i]
        right -= A[i]

        if left == right {
            splitIndex = i + 1
            score += 1
            break
        }
    }

    if splitIndex != -1 {
        score += max(solution(A[0..<splitIndex].map { $0 }), solution(A[splitIndex..<A.count].map { $0 }))
    }
    return score

}

let T = Int(readLine()!)!

for i in 0..<T {
    let N = Int(readLine()!)!
    let A = readLine()!.components(separatedBy: " ").map { Int($0)! }
    print(solution(A))
}
