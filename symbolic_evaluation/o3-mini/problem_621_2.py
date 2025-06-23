import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the constant: -π/2
# Step 1: Access mpmath's pi constant
pi_val = mp.pi

# Step 2: Divide pi by 2
half_pi = pi_val / 2

# Step 3: Apply negative sign
result = -half_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))