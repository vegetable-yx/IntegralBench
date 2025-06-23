import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 for intermediate calculations

# Calculate natural logarithm of 2 using mpmath's log function
result = mp.log(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))