import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute constants
sqrt2 = mp.sqrt(2)
sqrt2_over_2 = sqrt2 / 2
ln2 = mp.log(2)
ln2_squared = ln2**2
pi = mp.pi

# Compute dilogarithm terms
li2_half = mp.polylog(2, 0.5)  # Li_2(1/2)
li2_minus = mp.polylog(2, 1 - 1/sqrt2)  # Li_2(1 - 1/sqrt(2))
li2_plus = mp.polylog(2, 1 + 1/sqrt2)   # Li_2(1 + 1/sqrt(2))

# Compute the expression inside the brackets
bracket_term1 = -pi * ln2_squared
bracket_term2 = 4 * ln2 * li2_half
bracket_term3 = -li2_minus + li2_plus
bracket = bracket_term1 + bracket_term2 + bracket_term3

# Multiply by sqrt(2)/2
result = sqrt2_over_2 * bracket

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))