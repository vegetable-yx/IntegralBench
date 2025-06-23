import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/4 by breaking into steps:
# Step 1: Retrieve the constant pi
pi_val = mp.pi

# Step 2: Define the denominator
denominator = 4

# Step 3: Compute the result as pi divided by 4
result = pi_val / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))