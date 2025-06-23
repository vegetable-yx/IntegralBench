import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi ** 2

# Divide by 4 to get the first term: π²/4
term1 = pi_squared / 4

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Multiply 2 * π * ln(2) to get the second term
term2 = 2 * mp.pi * ln2

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))