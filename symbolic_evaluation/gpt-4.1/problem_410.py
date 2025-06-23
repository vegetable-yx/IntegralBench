import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute e raised to the power of -1
exp_neg1 = mp.exp(-1)

# Multiply the results by 1/2
result = 0.5 * sqrt_pi * exp_neg1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))