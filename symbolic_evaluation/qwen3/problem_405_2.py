import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^4 using mpmath function
exp_term = mp.exp(4)

# Subtract 1 from the exponential term
result = exp_term - 1

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))