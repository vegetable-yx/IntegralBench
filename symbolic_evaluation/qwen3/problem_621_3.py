import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate pi divided by two
pi_over_2 = mp.pi / 2

# Apply negative sign to get final result
result = -pi_over_2

print(mp.nstr(result, n=10))