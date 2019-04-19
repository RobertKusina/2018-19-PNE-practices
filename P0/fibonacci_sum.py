# We use the name variable assignments as in "fibonacci.py"


def fibonacci(num):
    num1 = 0
    num2 = 1
    counter = 0
    for i in range(num+1):
        counter += 1
        num1, num2 = num2, (num1 + num2)
    return counter

# Second part, the sum of all the terms selected


term = int(input("Up to which fibonacci's term you want to do the sum?:_"))
fib_term = fibonacci(term)
print("The addition of the first", term, "terms equals to: ", fib_term)
