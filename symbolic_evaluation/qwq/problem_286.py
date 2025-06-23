import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Divide by 92 to compute the final result
result = pi_squared / 92

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))