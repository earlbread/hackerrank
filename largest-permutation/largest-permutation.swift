import Foundation

var inputs = [[Int]]()

inputs.append(readLine()!.components(separatedBy: " ").map({ Int($0)! }))
inputs.append(readLine()!.components(separatedBy: " ").map({ Int($0)! }))

let n = inputs[0][0]
var k = inputs[0][1]

var array = inputs[1]

for i in 0..<array.count {
    guard k > 0 else {
        break
    }
    let (maxIndex, maxValue) = array.dropFirst(i)
                                    .enumerated()
                                    .max(by: { $0.element < $1.element })!

    if maxValue > array[i] {
        swap(&array[i], &array[maxIndex + i])
        k -= 1
    }
}

for element in array {
    print(element, terminator: " ")
}
