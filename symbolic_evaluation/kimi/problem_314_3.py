import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate negative of Catalan's constant
result = -mp.catalan

# Print result to 10 decimal places
print(mp.nstr(result, n=10))