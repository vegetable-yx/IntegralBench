import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Compute 1 + sqrt(2)
inner_sum = 1 + sqrt2

# Step 3: Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(inner_sum)

# Step 4: Square the logarithm
log_sq = log_val ** 2

# Step 5: Multiply by 1/2
result = 0.5 * log_sq

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))