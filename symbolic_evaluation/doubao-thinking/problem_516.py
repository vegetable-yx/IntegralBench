import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Step 1: Calculate π (pi)
pi_val = mp.pi

# Step 2: Compute π/2
half_pi = pi_val / 2

# Step 3: Subtract 1 to get the final result
result = half_pi - 1

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))