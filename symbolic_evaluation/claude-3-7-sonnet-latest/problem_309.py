import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Step 1: Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Step 2: Compute 1 + sqrt(2)
one_plus_sqrt2 = 1 + sqrt2

# Step 3: Compute natural logarithm of (1 + sqrt(2))
log_val = mp.log(one_plus_sqrt2)

# Step 4: Multiply by 2*pi
result = 2 * mp.pi * log_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))