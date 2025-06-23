import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 3
ln3 = mp.log(3)

# Multiply by pi to get the numerator
pi_times_ln3 = mp.pi * ln3

# Divide by 32 to get the final result
result = pi_times_ln3 / 32

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))