import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute constants
sqrt2 = mp.sqrt(2)
inv_sqrt2 = 1 / sqrt2

# Compute the four dilogarithm terms
Li1 = mp.polylog(2, -inv_sqrt2)  # Li_2(-1/sqrt(2))
Li2 = mp.polylog(2, inv_sqrt2)   # Li_2(1/sqrt(2))
Li3 = mp.polylog(2, 1 - sqrt2)   # Li_2(1 - sqrt(2))
Li4 = mp.polylog(2, 1 + sqrt2)   # Li_2(1 + sqrt(2))

# Combine terms according to the expression
term1 = -4 * Li1
term2 = 4 * Li2
term3 = Li3
term4 = -Li4

# Sum all terms and divide by 16
total = term1 + term2 + term3 + term4
result = total / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))