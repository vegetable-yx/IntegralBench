import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# Compute individual components of the expression
# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Compute the dilogarithm (polylog of order 2) at 1/2
li2_half = mp.polylog(2, 0.5)

# Compute the trilogarithm (polylog of order 3) at 1/2
li3_half = mp.polylog(3, 0.5)

# Calculate π²
pi_squared = mp.pi**2

# Compute each term in the expression:
# Term 1: 4 * Li₃(1/2)
term1 = 4 * li3_half

# Term 2: -4 * ln(2) * Li₂(1/2)
term2 = -4 * ln2 * li2_half

# Term 3: π² * ln(2)
term3 = pi_squared * ln2

# Term 4: -2 * [ln(2)]³
term4 = -2 * (ln2**3)

# Sum all terms and divide by 64
result = (term1 + term2 + term3 + term4) / 64

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))