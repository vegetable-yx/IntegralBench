import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Get the value of π
pi_val = mp.pi

# Step 2: Square π
pi_squared = pi_val ** 2

# Step 3: Divide by 4 to get the result
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))