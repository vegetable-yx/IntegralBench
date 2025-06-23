import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate base 2 raised to the power of 4/3
power_part = mp.power(2, 4/3)

# Multiply by 1/4 to get the final result
result = (1/4) * power_part

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))