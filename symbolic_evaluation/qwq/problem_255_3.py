import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate the constant pi using mpmath's built-in constant
pi_value = mp.pi

# Multiply pi by -3 to get the final result
result = -3 * pi_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))