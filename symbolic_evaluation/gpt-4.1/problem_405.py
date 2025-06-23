import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute e raised to the power of 4
exp_value = mp.exp(4)

# Subtract 1 from the exponential value
result = exp_value - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))