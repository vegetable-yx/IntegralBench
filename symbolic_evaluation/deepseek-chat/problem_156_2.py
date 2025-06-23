import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Calculate first term: π²/12
term1 = pi_squared / 12

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Square the logarithm
ln2_squared = ln2 ** 2

# Calculate second term: (ln²2)/2
term2 = ln2_squared / 2

# Combine terms: π²/12 - (ln²2)/2
result = term1 - term2

# Print result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))