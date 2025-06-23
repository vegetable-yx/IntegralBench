import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the golden ratio (1 + sqrt(5))/2
golden_ratio = (1 + sqrt5) / 2

# Calculate the natural logarithm of the golden ratio
log_value = mp.log(golden_ratio)

# Multiply by 1/2 of pi
pi_half = mp.pi / 2
result = pi_half * log_value

# Print result with 10 decimal places
print(mp.nstr(result, n=10))