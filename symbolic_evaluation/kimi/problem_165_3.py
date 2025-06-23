import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e^-2 using mpmath's exponential function
exp_term = mp.exp(-2)

# Multiply by the exponential term and divide by 2
result = (mp.pi / 2) * exp_term

# Print the result with 10 decimal places using mpmath's number string function
print(mp.nstr(result, n=10))