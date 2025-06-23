import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate e raised to the power of 4
exp_val = mp.exp(4)

# Calculate 2 * pi
two_pi = 2 * mp.pi

# Multiply the two components to get the final result
result = two_pi * exp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))