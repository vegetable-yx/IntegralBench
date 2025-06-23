import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Step 1: Calculate π using mpmath constant
pi_val = mp.pi

# Step 2: Compute π/2
half_pi = pi_val / 2

# Step 3: Calculate square root of (π/2)
result = mp.sqrt(half_pi)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))