def is_power_of_8(n):
    if n < 1:
        return False
    while n % 8 == 0:
        n = n // 8
    return n == 1

number = 512
if is_power_of_8(number):
    print(number, "is a power of 8")
else:
    print(number, "is NOT a power of 8")
