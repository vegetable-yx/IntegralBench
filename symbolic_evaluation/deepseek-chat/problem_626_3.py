import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute π using mpmath's constant
pi_val = mp.pi

# Step 2: Compute π/2
half_pi = pi_val / 2

# Step 3: Compute the natural logarithm of (π/2)
result = mp.log(half_pi)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))