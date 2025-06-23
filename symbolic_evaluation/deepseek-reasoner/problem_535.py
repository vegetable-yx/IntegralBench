import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e^3 using mpmath exponential function
e_cubed = mp.exp(3)

# Divide the result by 3 to get the final value
result = e_cubed / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))