import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Assign mathematical constant e to result variable
result = mp.e

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))