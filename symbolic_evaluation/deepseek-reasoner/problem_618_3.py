import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Compute Euler-Mascheroni constant using mpmath's built-in constant
euler_mascheroni = mp.euler

# Calculate the final value 1 - γ
result = 1 - euler_mascheroni

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))