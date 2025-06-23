import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Precompute common constants and expressions
sqrt2 = mp.sqrt(2)  # √2
a = 1 + sqrt2       # 1 + √2
b = mp.log(a)       # ln(1 + √2)
c = 1 - 1/sqrt2     # 1 - 1/√2
d = -1 / a          # -1/(1 + √2)

# Compute each term in the expression
term1 = sqrt2 * (b ** 3)                   # √2 * ln³(1+√2)
term2 = mp.pi * (b ** 2)                   # π * ln²(1+√2)
term3 = 4 * b * mp.polylog(2, c)           # 4 * ln(1+√2) * Li₂(1 - 1/√2)
term4 = 4 * mp.polylog(3, c)               # 4 * Li₃(1 - 1/√2)
term5 = 4 * mp.polylog(3, d)               # 4 * Li₃(-1/(1+√2))

# Combine terms and multiply by 1/8
total = term1 - term2 - term3 + term4 - term5
result = total / 8

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))