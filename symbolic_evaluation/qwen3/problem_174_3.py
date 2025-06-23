import mpmath as mp
mp.dps = 15

# Compute the argument for the dilogarithm
x = mp.mpf(1)/16

# Calculate the dilogarithm Li_2(1/16)
li2_term = mp.polylog(2, x)

# Compute π divided by 4
pi_quarter = mp.pi / 4

# Multiply components to get final result
result = pi_quarter * li2_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))