import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate e^2 using mpmath exponential function
e_squared = mp.exp(2)

# Compute the numerator (e^2 - 1)
numerator = e_squared - 1

# Calculate final result by dividing numerator by 4
result = numerator / 4

# Print result with 10 decimal places using mpmath string formatting
print(mp.nstr(result, n=10))