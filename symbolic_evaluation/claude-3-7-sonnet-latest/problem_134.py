import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is 2π
# Break into steps for clarity:
# Step 1: Define the constant factor 2
factor = mp.mpf(2)

# Step 2: Multiply the factor by π to get the result
result = factor * mp.pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))