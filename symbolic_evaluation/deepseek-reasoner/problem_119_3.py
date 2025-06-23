import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 8 to get the final result
result = mp.fdiv(pi_squared, 8)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))