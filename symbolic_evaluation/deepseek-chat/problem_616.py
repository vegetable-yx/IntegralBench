import mpmath as mp

# Set internal decimal places to 15 for high precision
mp.dps = 15

# Calculate (ln(2))^2
ln2 = mp.log(2)  # Natural logarithm of 2
ln2_sq = ln2 ** 2  # Square of ln(2)

# First term: (ln(2))^2 divided by 4
term1 = ln2_sq / 4

# Second term: π^2 divided by 24
pi_sq = mp.pi ** 2  # Square of π
term2 = pi_sq / 24

# Sum both terms to get final result
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))