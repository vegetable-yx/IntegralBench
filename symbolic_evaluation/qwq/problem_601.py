import mpmath as mp
mp.dps = 15  # Set decimal places for internal precision

# Calculate natural logarithm of 2 using mpmath's log function
ln2 = mp.log(2)

# Multiply by the logarithm result using mpmath's pi constant
result = mp.pi * ln2

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))