def square(number):
    return number ** 2
print(square(5))
print(square(10))
print(square(12))
print(square(square(2)))
square(int('2'))

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

sum_numbers(5,10)
sum_numbers(50, 100)

square(sum_numbers(5,5))