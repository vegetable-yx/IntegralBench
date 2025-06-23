import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate natural logarithm of 3 using mpmath's log function
result = mp.log(3)

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))