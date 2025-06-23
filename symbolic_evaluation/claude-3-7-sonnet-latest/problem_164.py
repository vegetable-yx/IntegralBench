import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute pi using mpmath constant
pi_val = mp.pi

# Calculate pi raised to the fourth power
pi_fourth = pi_val ** 4

# Multiply by the coefficient 7
result = 7 * pi_fourth

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))