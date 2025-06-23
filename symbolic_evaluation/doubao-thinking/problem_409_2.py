import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate natural logarithm of 2
result = mp.log(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))