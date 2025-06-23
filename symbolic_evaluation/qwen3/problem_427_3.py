import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 11
sqrt_11 = mp.sqrt(11)

# Multiply by 11 to get numerator
numerator = 11 * sqrt_11

# Divide by denominator 18
result = numerator / 18

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))