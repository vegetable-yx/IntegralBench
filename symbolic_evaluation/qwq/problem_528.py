import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e (Euler's number)
e_constant = mp.e

# Compute the exponent (e - 1)
exponent = e_constant - 1

# Calculate e raised to the (e-1) power
e_power = mp.exp(exponent)

# Final result by subtracting e from the computed power
result = e_power - e_constant

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))