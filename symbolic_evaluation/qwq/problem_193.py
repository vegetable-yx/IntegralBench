import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π^2 using mpmath's pi constant
pi_squared = mp.pi ** 2

# Calculate the first term (π²/16)
term1 = pi_squared / 16

# Calculate natural logarithm of 2 using mpmath
ln2 = mp.log(2)

# Multiply components to get final result
result = term1 * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))