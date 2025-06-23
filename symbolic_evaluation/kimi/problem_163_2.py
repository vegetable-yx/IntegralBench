import mpmath as mp
mp.dps = 15  # Set decimal precision to 15 for intermediate calculations

# Calculate natural logarithm of 2 using mpmath's log function
ln2 = mp.log(2)

# Multiply by the given constant coefficient
coefficient = mp.mpf('1.96875')
result = coefficient * ln2

# Print the final result with 10 decimal precision
print(mp.nstr(result, n=10))