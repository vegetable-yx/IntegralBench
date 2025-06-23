import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2
ln_2 = mp.log(2)

# Square the logarithm value
ln_2_squared = ln_2 ** 2

# Multiply by pi
pi_times_squared = mp.pi * ln_2_squared

# Divide by 4 to get final result
result = pi_times_squared / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))