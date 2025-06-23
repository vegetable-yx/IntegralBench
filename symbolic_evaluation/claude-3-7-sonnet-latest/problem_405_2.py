import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e raised to the power of 4
exp_val = mp.exp(4)

# Subtract 1 from the exponential value
result = exp_val - 1

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))