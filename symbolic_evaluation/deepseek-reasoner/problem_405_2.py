import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^4 using mpmath's exponential function
exp_4 = mp.exp(4)

# Subtract 1 from the computed exponential value
result = exp_4 - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))