import mpmath as mp
mp.dps = 15  # Set decimal precision for intermediate calculations

# Calculate pi squared
pi_squared = mp.power(mp.pi, 2)

# Divide by 8 to get final result
result = pi_squared / 8

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))