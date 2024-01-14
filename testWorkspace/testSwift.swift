func isPalindrome(_ number: Int) -> Bool {
    let numberString = String(number)
    let reversedString = String(numberString.reversed())
    return numberString == reversedString
}

// Exemples d'utilisation
let number1 = 121
let number2 = 12321

print(isPalindrome(number1))