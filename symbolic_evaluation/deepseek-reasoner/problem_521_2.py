import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate natural logarithm of 3
result = mp.log(3)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))