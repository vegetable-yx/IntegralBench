import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate components of the numerator
sqrt3 = mp.sqrt(3)  # Compute square root of 3
term1 = 48 - 25 * sqrt3  # First constant term
term2 = mp.pi * (4 * sqrt3 - 3)  # Pi-related term

# Combine terms and compute final result
numerator = term1 + term2
result = numerator / 96

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))