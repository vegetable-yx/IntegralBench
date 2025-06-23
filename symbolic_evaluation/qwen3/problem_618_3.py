import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Get Euler-Mascheroni constant
gamma_val = mp.euler

# Calculate 1 - gamma
result = 1 - gamma_val

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))