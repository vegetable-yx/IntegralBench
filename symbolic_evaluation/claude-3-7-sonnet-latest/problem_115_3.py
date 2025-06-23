import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Get the value of pi
pi_val = mp.pi

# Step 2: Square pi
pi_squared = pi_val ** 2

# Step 3: Divide by 8
result = pi_squared / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))