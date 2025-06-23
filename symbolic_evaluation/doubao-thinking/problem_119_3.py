import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Step 1: Calculate pi squared
pi_squared = mp.pi ** 2

# Step 2: Divide by 8 to get the result
result = pi_squared / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))