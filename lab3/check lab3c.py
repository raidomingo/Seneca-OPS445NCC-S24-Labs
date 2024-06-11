
import lab3c
print(lab3c.operate(10, 20, 'add'))
# Will return 30
print(lab3c.operate(2, 3, 'add'))
# Will return 5
print(lab3c.operate(100, 5, 'subtract'))
# Will return 95
print(lab3c.operate(10, 20, 'subtract'))
# Will return -10
print(lab3c.operate(5, 5, 'multiply'))
# Will return 25
print(lab3c.operate(10, 100, 'multiply'))
# Will return 1000
print(lab3c.operate(100, 5, 'divide'))
# Will return Error: function operator can be "add", "subtract", or "multiply"
print(lab3c.operate(100, 5, 'power'))
# Will return Error: function operator can be "add", "subtract", or "multiply"