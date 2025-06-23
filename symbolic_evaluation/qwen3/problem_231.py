import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate square root of 2 using mpmath
result = mp.sqrt(2)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))