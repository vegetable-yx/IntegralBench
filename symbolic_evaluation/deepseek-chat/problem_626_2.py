import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Step 1: Compute the mathematical constant π
pi_val = mp.pi

# Step 2: Divide π by 2
pi_over_2 = pi_val / 2

# Step 3: Compute the natural logarithm of the result
result = mp.log(pi_over_2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))