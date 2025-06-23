import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Divide by 6 to get the final result
result = pi_squared / 6

# Print the result with 10 decimal precision
print(mp.nstr(result, n=10))