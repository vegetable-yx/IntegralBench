import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^4
exp_val = mp.exp(4)

# Subtract 1 from the result
result = exp_val - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))