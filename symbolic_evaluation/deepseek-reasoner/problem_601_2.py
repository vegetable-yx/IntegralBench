import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi to get the final result
result = mp.pi * ln2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))