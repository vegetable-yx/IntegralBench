import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the coefficient and pi value
coefficient = 506
pi_value = mp.pi

# Multiply coefficient by pi to get the final result
result = coefficient * pi_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))