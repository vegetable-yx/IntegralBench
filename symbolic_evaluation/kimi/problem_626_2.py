import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate natural logarithm of 2 using mpmath's log function
result = mp.log(2)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))