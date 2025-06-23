import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^4 using mpmath's exponential function
exp_4 = mp.exp(4)

# Subtract 1 from the result of e^4
result = exp_4 - 1

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))