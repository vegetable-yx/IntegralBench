import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^4 using mpmath's exponential function
exp_term = mp.exp(4)

# Subtract 1 from the exponential term
result = exp_term - 1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))