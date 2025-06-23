import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define constants and necessary values
pi = mp.pi
ln2 = mp.log(2)  # Natural logarithm of 2

# Compute Li_2(1/2) - dilogarithm of 1/2
li2_half = mp.polylog(2, 0.5)

# Compute Li_3(1/2) - trilogarithm of 1/2
li3_half = mp.polylog(3, 0.5)

# Calculate each term in the expression
# First term: π^3 / 48
term1 = (pi ** 3) / 48

# Second term: (π / 8) * (ln(2))^2
term2 = (pi / 8) * (ln2 ** 2)

# Third term: - (1/2) * ln(2) * Li_2(1/2)
term3 = -0.5 * ln2 * li2_half

# Fourth term: (1/2) * Li_3(1/2)
term4 = 0.5 * li3_half

# Sum all terms to get the result
result = term1 + term2 + term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))