import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# First term: π² divided by 24
term1 = pi_squared / 24

# Natural logarithm of 2
ln2 = mp.log(2)

# Square of ln(2)
ln2_squared = ln2 ** 2

# Second term: (1/2) times the square of ln(2)
term2 = (mp.mpf(1)/2) * ln2_squared

# Combine terms: π²/24 - (1/2)ln²(2)
result = term1 - term2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))