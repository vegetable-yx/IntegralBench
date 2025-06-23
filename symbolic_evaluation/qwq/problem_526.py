import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply by pi
pi_times_ln3 = mp.pi * ln3

# Divide by 4 to get final result
result = pi_times_ln3 / 4

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))