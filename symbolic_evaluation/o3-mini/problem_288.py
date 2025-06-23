import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute frequently used constants
sqrt2 = mp.sqrt(2)
ln_arg = 1 + sqrt2
ln_val = mp.log(ln_arg)  # ln(1 + sqrt(2))

# Compute polylog arguments
arg1 = -1 / sqrt2  # -1/sqrt(2)
arg2 = 1 / sqrt2   # 1/sqrt(2)

# Compute polylog terms
Li2_term = mp.polylog(2, arg1)  # Li₂(-1/sqrt(2))
Li3_term1 = mp.polylog(3, arg1) # Li₃(-1/sqrt(2))
Li3_term2 = mp.polylog(3, arg2) # Li₃(1/sqrt(2))

# Compute each term in the expression
term1 = 6 * mp.pi * (ln_val ** 2)               # 6π ln²(1+√2)
term2 = -16 * ln_val * Li2_term                 # -16 ln(1+√2) Li₂(-1/√2)
term3 = 8 * Li3_term1                           # 8 Li₃(-1/√2)
term4 = -8 * Li3_term2                          # -8 Li₃(1/√2)
term5 = mp.pi ** 3                              # π³

# Combine terms and divide by 96
result = (term1 + term2 + term3 + term4 + term5) / 96

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))