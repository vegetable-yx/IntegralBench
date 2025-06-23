import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Multiply by the coefficient 506
result = 506 * pi_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))