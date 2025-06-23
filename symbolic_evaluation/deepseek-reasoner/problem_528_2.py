import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate Euler's number (base of natural logarithm)
e_value = mp.e

# Compute the exponent (e - 1)
exponent = e_value - 1

# Calculate e raised to the (e - 1) power
exp_term = mp.exp(exponent)

# Final result calculation: e^(e-1) - e
result = exp_term - e_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))