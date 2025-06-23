import mpmath as mp

# Set decimal places for internal calculation
mp.dps = 15

# Common constants and expressions
sqrt2 = mp.sqrt(2)
ln_term = mp.log(1 + sqrt2)  # ln(1 + sqrt(2))

# Arguments for polylogarithms
arg1 = 2 - sqrt2  # 2 - sqrt(2)
arg2 = sqrt2 - 1  # sqrt(2) - 1

# Compute polylog terms
Li3_diff = mp.polylog(3, arg1) - mp.polylog(3, arg2)
Li2_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)

# Compute individual terms of the expression
term1 = 16 * Li3_diff
term2 = -8 * ln_term * Li2_diff
term3 = ln_term**3
term4 = 6 * mp.pi**2 * ln_term
term5 = 48 * mp.zeta(3)

# Combine all terms and multiply by 1/96
result = (term1 + term2 + term3 + term4 + term5) / 96

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))