import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi (using mpmath's constant for pi)
result = mp.pi * ln2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))