import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute 1 + sqrt(2)
sum_val = 1 + sqrt2

# Natural logarithm of the sum
log_val = mp.log(sum_val)

# Compute pi divided by 2
pi_half = mp.pi / 2

# Multiply to get the final result
result = pi_half * log_val

print(mp.nstr(result, n=10))