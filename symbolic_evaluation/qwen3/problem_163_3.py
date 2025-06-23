import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi using mpmath's constant
pi_value = mp.pi

# Compute pi cubed
pi_cubed = mp.power(pi_value, 3)

# Multiply by 2 to get the final result
result = 2 * pi_cubed

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))