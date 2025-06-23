import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Multiply by coefficient 5
numerator = 5 * sqrt2

# Multiply by pi
product = numerator * mp.pi

# Divide by 8 to get final result
result = product / 8

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))