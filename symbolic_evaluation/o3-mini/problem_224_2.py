import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the constant sqrt(2)
sqrt2 = mp.sqrt(2)

# Calculate the argument for the logarithm: 3 + 2*sqrt(2)
log_arg = 3 + 2 * sqrt2

# Compute natural logarithm of the argument
log_val = mp.log(log_arg)

# Square the logarithm
log_sq = log_val ** 2

# Compute the first term: (π/8) * [ln(3 + 2√2)]^2
term1 = (mp.pi / 8) * log_sq

# Calculate the arguments for the dilogarithms
x1 = 1 / sqrt2   # 1/√2
x2 = -1 / sqrt2  # -1/√2

# Compute the dilogarithms
li2_pos = mp.polylog(2, x1)   # Li_2(1/√2)
li2_neg = mp.polylog(2, x2)   # Li_2(-1/√2)

# Compute the difference between the dilogarithms
diff_li2 = li2_pos - li2_neg

# Compute the second term: (1/4) * [Li_2(1/√2) - Li_2(-1/√2)]
term2 = (1/4) * diff_li2

# Sum both terms to get the final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))