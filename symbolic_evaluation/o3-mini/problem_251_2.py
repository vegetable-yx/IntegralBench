import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt_val = mp.sqrt(2)

# Step 2: Add 1 to the square root of 2
sum_val = 1 + sqrt_val

# Step 3: Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(sum_val)

# Step 4: Multiply the logarithm by pi
result = mp.pi * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))