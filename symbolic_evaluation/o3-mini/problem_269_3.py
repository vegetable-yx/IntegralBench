import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant terms
# First term: -π³ / 144
term1 = - (mp.pi ** 3) / 144

# Second term: π² * √3 / 24
term2 = (mp.pi ** 2 * mp.sqrt(3)) / 24

# Third term: -π / 8
term3 = -mp.pi / 8

# Arguments for the dilogarithm functions
sqrt3 = mp.sqrt(3)
arg1 = (1 + sqrt3) / 3  # (1 + √3)/3
arg2 = (1 - sqrt3) / 3  # (1 - √3)/3

# Compute the dilogarithms: Li₂(arg1) and Li₂(arg2)
dilog1 = mp.polylog(2, arg1)
dilog2 = mp.polylog(2, arg2)

# Difference of dilogarithms
diff_dilog = dilog1 - dilog2

# Fourth term: (1/32) * [Li₂(arg1) - Li₂(arg2)]
term4 = diff_dilog / 32

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))