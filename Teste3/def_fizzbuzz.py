def funcao (num1):
    div1 = num1 % 3
    div2 = num1 % 5
    if div1 == 0 and div2 == 0:
        return "FizzBuzz"
    if div1 == 0:
        return "Fizz"
    if div2 == 0:
        return "Buzz"
    return num1

print(funcao(8))