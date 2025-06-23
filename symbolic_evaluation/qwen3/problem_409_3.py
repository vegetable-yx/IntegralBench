import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate natural logarithm of 2 using mpmath's log function
result = mp.log(2)

# Print result with exactly 10 decimal places using nstr formatting
print(mp.nstr(result, n=10))