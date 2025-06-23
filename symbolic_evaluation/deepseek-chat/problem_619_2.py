import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute π (pi) using mpmath's constant
pi_val = mp.pi

# Step 2: Square π to get π²
pi_squared = pi_val**2

# Step 3: Divide π² by 8 to get the result
result = pi_squared / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))