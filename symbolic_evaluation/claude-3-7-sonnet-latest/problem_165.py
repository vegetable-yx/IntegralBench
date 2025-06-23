import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^{-2.0}
exp_val = mp.exp(-2.0)

# Multiply by pi to get the result
result = mp.pi * exp_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))