import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the square root term: √120
sqrt_120 = mp.sqrt(120)

# Compute the first multiplicative part: 11 + √120
part1 = 11 + sqrt_120

# Access pi constant from mpmath
pi = mp.pi

# Compute the terms in the second part:
# term1 = π²/64
term1 = (pi ** 2) / 64
# term2 = π/16
term2 = pi / 16
# term3 = 1/8
term3 = mp.mpf(1) / 8

# Sum the terms to form the second multiplicative part
part2 = term1 + term2 + term3

# Multiply the two parts to get the final result
result = part1 * part2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))