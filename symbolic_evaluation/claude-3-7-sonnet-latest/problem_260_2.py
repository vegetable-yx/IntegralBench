import mpmath as mp

# Set the internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi to get the result: π * ln(2)
result = mp.pi * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))