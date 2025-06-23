import mpmath as mp
mp.dps = 15  # Set precision to 15 decimal places for internal calculations

# Calculate Catalan's constant
G = mp.catalan

# Multiply by 2 to get the final result
result = 2 * G

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))