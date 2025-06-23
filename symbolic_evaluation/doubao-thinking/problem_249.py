import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute (sqrt(5) - 2)
numerator_part = sqrt5 - 2

# Multiply by pi and divide by 2
result = (mp.pi * numerator_part) / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))