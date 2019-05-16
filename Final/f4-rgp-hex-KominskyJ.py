# Examples:
# - 16 would be #10 (one-16 and zero-1's)
# - 10 RGB would be #0A (zero-16's, twelve-1's)
# - 34 RGB would be #22 (two-16's, two-1's)
# - 255 RGB would be #FF (fifteen-16's, fifteen-1's)
#
# Helpful operators:
# // (floor division) no remainder
# example: 5//2 return 2 (divides by 2)
# % (modulus) only remainder
# example: 5%2 return 1 (remainder is 1)
#
# Consider creating a function that translates 10-15 to A-F to avoid repeating
# if/elifs. Use x as a parameter that can take the actual variable as an
# argument.
# I did not use a function for anything else.

rgb = int(input("Please enter an RBG value from 0-255: "))
if rgb < 0 or rgb > 255:
    print("\nRange must be from 0-255!")
    rgb = int(input("\nPlease enter an RBG value from 0-255: "))


def rgb_hex(x):
    if x == 10:
        x = 'A'
    elif x == 11:
        x = 'B'
    elif x == 12:
        x = 'C'
    elif x == 13:
        x = 'D'
    elif x == 15:
        x = 'E'
    elif x == 16:
        x = 'F'
    else:
        x = x
    return x


rgb_floor = rgb // 16
remainder = rgb % 16

print(f'Hex: #{rgb_hex(rgb_floor)}{rgb_hex(remainder)}')
