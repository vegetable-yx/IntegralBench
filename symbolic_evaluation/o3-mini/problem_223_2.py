import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate π (pi) once for reuse
pi = mp.pi

# Calculate ln(2) - natural logarithm of 2
ln2 = mp.log(2)

# Compute ln²(2) = (ln(2))^2
ln2_squared = ln2 ** 2

# Calculate term1: π³ / 48
term1 = (pi ** 3) / 48

# Calculate term2: (π / 8) * ln²(2)
term2 = (pi / 8) * ln2_squared

# Calculate term3: (1/4) * Li₃(1/2) where Li₃ is the trilogarithm (polylog(3, x))
term3 = (1/4) * mp.polylog(3, 0.5)

# Sum all terms to get the final result
result = term1 + term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))