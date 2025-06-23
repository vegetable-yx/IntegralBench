import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Compute (1 + sqrt(2))
one_plus_sqrt2 = 1 + sqrt2

# Step 3: Compute the natural logarithm of (1 + sqrt(2))
log_val = mp.log(one_plus_sqrt2)

# Step 4: Multiply the logarithm by pi
result = mp.pi * log_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))