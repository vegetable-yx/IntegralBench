import mpmath as mp
mp.dps = 15  # Set decimal precision

# Calculate the analytical result
result = mp.mpf(1)  # Direct assignment of the exact solution

# Print result with 10 decimal places
print(mp.nstr(result, n=10))