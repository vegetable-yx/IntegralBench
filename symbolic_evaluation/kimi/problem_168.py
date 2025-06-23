import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi squared using mpmath's constant
pi_squared = mp.pi ** 2

# Final result with 10 decimal precision
print(mp.nstr(pi_squared, n=10))