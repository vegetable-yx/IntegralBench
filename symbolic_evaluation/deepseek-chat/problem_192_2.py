import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi cubed divided by 48
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 48

# Calculate natural logarithm of 2
ln2 = mp.log(2)
# Square the natural logarithm
ln2_squared = ln2 ** 2
# Multiply by pi/4
term2 = (mp.pi / 4) * ln2_squared

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))