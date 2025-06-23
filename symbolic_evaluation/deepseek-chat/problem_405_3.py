import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute e raised to the power of 4
exp_val = mp.exp(4)

# Subtract 1 from the result
result = exp_val - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))