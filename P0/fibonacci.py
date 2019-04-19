# Finally committing this
#Since Fibonacci's terms are all an addition, we start with the first number a 0 to be added to the second


def fibonacci(num):
    num1 = 0
    num2 = 1
    for i in range(num):
        num1, num2 = num2, (num1 + num2)
    return num1


while True:
    term = int(input("Which Fibonacci's nth term you want to calculate?"))
    fibterm = fibonacci(term)
    print(fibterm)
