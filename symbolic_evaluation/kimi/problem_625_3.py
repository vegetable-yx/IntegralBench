import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Assign the mathematical constant π directly
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))