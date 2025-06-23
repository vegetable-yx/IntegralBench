import mpmath as mp
mp.dps = 15

# Calculate e^4 using mpmath's exp function
exp_val = mp.exp(4)

# Subtract 1 from the computed exponential value
result = exp_val - 1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))