import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the exact value of the integral which is 3π
pi_value = mp.pi  # Get π from mpmath
result = 3 * pi_value  # Multiply by 3 to get the final result

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))