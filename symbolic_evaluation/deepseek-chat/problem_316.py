import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute pi squared
pi_squared = mp.pi ** 2

# Step 2: Divide by 12 to get the result
result = pi_squared / 12

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))