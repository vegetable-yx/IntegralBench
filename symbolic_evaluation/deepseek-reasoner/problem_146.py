import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 2 to get final result
result = pi_squared / 2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))