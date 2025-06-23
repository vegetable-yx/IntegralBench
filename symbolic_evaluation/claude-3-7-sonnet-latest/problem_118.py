import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Step 1: Get the value of pi
pi_val = mp.pi

# Step 2: Compute pi cubed
pi_cubed = pi_val ** 3

# Step 3: Divide pi_cubed by 4 to get the result
result = pi_cubed / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))