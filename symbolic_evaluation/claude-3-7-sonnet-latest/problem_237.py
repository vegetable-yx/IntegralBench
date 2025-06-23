import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Step 1: Compute π using mpmath's constant
pi_val = mp.pi

# Step 2: Square π
pi_squared = pi_val ** 2

# Step 3: Divide by 2 to get the result
result = pi_squared / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))