def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'

print(describe_temperature(50))
# Will return 'hot'
print(describe_temperature(20))
# Will return 'perfect'
print(describe_temperature(-50))
# Will return 'cold'
print(describe_temperature(25))
# Will return 'ok'
print(describe_temperature(10))
# Will return 'ok'