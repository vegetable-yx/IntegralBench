import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute frequently used constants
sqrt2 = mp.sqrt(2)
ln_val = mp.log(1 + sqrt2)  # ln(1 + √2)

# Compute the polylog terms
Li3_pos = mp.polylog(3, 1/sqrt2)   # Li₃(1/√2)
Li3_neg = mp.polylog(3, -1/sqrt2)  # Li₃(-1/√2)

# Compute the dilogarithm differences
Li2_half = mp.polylog(2, 0.5)      # Li₂(1/2)
Li2_neg_half = mp.polylog(2, -0.5) # Li₂(-1/2)
dilog_diff = Li2_half - Li2_neg_half

# Compute each term of the main expression
term1 = mp.pi * ln_val**3           # π·ln³(1+√2)
term2 = 6 * Li3_pos                 # 6·Li₃(1/√2)
term3 = -6 * Li3_neg                # -6·Li₃(-1/√2)
term4 = -3 * ln_val * dilog_diff    # -3·ln(1+√2)·[Li₂(1/2)-Li₂(-1/2)]

# Sum all terms and multiply by 1/8
total = term1 + term2 + term3 + term4
result = total / 8

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))