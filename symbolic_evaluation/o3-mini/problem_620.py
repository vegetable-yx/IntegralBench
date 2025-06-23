import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply pi and ln(2)
pi_ln2 = mp.pi * ln2

# Divide by 8 to get final result
result = pi_ln2 / 8

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))