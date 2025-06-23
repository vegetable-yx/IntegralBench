import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the arcsin of 1/4
a = mp.asin(0.25)

# Compute the square of the arcsin value
a_sq = a**2

# Calculate the square root of 15
sqrt15 = mp.sqrt(15)

# Compute the argument for the logarithm: (sqrt(15) + 1)/4
log_arg = (sqrt15 + 1) / 4

# Calculate the logarithm term: ln((sqrt(15)+1)/4)
log_term = mp.log(log_arg)

# Compute the two arguments for the dilogarithm functions
arg1 = 0.5 - sqrt15 / 4  # 1/2 - sqrt(15)/4
arg2 = 0.5 + sqrt15 / 4  # 1/2 + sqrt(15)/4

# Compute the two dilogarithm terms: Li2(1/2 - sqrt(15)/4) and Li2(1/2 + sqrt(15)/4)
li2_term1 = mp.polylog(2, arg1)
li2_term2 = mp.polylog(2, arg2)

# Combine all terms according to the expression:
# (1/8) * [ pi * a^2 - 2*a*log_term + li2_term1 - li2_term2 ]
result = (mp.pi * a_sq - 2 * a * log_term + li2_term1 - li2_term2) / 8

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))