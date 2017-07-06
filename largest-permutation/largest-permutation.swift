import Foundation

var inputs = [[Int]]()

inputs.append(readLine()!.components(separatedBy: " ").map({ Int($0)! }))
inputs.append(readLine()!.components(separatedBy: " ").map({ Int($0)! }))

let n = inputs[0][0]
var k = inputs[0][1]

var array = inputs[1]

var positions = [Int: Int]()

for (index, value) in array.enumerated() {
    positions[value] = index
}

for i in 0..<array.count {
    if k == 0 {
        break
    }

    if array[i] == (n - i) {
        continue
    }

    let maxIndex = positions[n - i]!
    positions[n - i] = i
    positions[array[i]] = maxIndex

    swap(&array[i], &array[maxIndex])
    k -= 1
}

print(array.map({ String($0) }).joined(separator: " "))
