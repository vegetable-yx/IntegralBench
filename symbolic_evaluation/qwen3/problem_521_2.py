import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 3 using mpmath's log function
result = mp.log(3)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))