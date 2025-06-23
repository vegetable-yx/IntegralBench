import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 2 using mpmath's log function
result = mp.log(2)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))