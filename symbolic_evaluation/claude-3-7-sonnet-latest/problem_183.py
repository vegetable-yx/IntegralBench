import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Compute the argument for the logarithm: 1 + sqrt(2)
log_arg = 1 + sqrt2

# Step 3: Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(log_arg)

# Step 4: Compute π/4
pi_over_4 = mp.pi / 4

# Step 5: Multiply π/4 by the logarithm result
result = pi_over_4 * log_val

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))