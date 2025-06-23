import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# First term: π² / 96
term1 = pi_squared / 96

# Compute the golden ratio conjugate: (1 + √5)/2
golden_ratio = (1 + mp.sqrt(5)) / 2

# Natural logarithm of the golden ratio
ln_golden = mp.log(golden_ratio)

# Square of the logarithm
ln_squared = ln_golden ** 2

# Second term: (1/32) * [ln(golden_ratio)]²
term2 = (1 / 32) * ln_squared

# Sum both terms
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))