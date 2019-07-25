def raise_to_power(base_num, power_num):
    result = 1
    for number in range(power_num):
        result *= base_num
    return result

print(raise_to_power(3,2))

for number in range(2):
    print(number)