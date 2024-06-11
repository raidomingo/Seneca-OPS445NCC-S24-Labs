def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3

number = return_number_value()
print(number)
print(number + 3)
print(return_number_value() + 10)

# print('Return value' + number)
print('Return value' + str(number))
print('Return value' + str(return_number_value()))