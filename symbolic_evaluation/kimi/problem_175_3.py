import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each term of the expression separately
# First term: -π^2 / 72
pi_squared = mp.power(mp.pi, 2)
term1 = -pi_squared / 72

# Second term: π√3 / 12
sqrt3 = mp.sqrt(3)
term2 = (mp.pi * sqrt3) / 12

# Third term: -1/4
term3 = -mp.mpf(1)/4

# Combine all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))