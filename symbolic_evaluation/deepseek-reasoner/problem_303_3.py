import mpmath as mp
mp.dps = 15

# Calculate constants and components
sqrt3 = mp.sqrt(3)
pi = mp.pi

# First term: π²/128
term1 = (pi ** 2) / 128

# Second term: (√3*π)/64
term2 = (sqrt3 * pi) / 64

# Third term components: 3√3/32 * arcsin(1/4)
asin_arg = mp.mpf(1)/4  # High-precision 1/4
asin_val = mp.asin(asin_arg)
term3 = (3 * sqrt3 / 32) * asin_val

# Combine all terms
result = term1 - term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))