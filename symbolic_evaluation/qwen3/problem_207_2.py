import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential of -1
exp_neg1 = mp.exp(-1)

# Combine components to compute final result
result = (sqrt_pi / 2) * exp_neg1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))