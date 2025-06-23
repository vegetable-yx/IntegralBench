import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute common constants and intermediate values
pi = mp.pi
ln2 = mp.log(2)  # Natural logarithm of 2

# Calculate each term of the expression separately
# Term 1: (π/3) * (ln(2))^2
term1 = (pi / 3) * (ln2 ** 2)

# Term 2: -(π/3) * ln(2)
term2 = - (pi / 3) * ln2

# Term 3: π/3
term3 = pi / 3

# Term 4: -2 * ln(2)
term4 = -2 * ln2

# Term 5: -2 * ln(√3 - 1)
# First compute √3
sqrt3 = mp.sqrt(3)
# Then compute the argument: √3 - 1
arg = sqrt3 - 1
# Compute ln(√3 - 1)
term5 = -2 * mp.log(arg)

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4 + term5

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))