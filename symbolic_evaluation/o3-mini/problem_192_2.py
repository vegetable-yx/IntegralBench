import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the argument for the logarithm: (sqrt(2) + 1) / 2
log_arg = (mp.sqrt(2) + 1) / 2

# Compute the natural logarithm and square it
log_val = mp.log(log_arg)
log_sq = log_val ** 2

# Compute the first term: (pi / 8) * (ln((sqrt(2)+1)/2))^2
term1 = (mp.pi / 8) * log_sq

# Compute arguments for the dilogarithm functions
arg1 = 1 - 1 / mp.sqrt(2)  # 1 - 1/sqrt(2)
arg2 = 1 + 1 / mp.sqrt(2)  # 1 + 1/sqrt(2)

# Compute the two dilogarithm values
li1 = mp.polylog(2, arg1)  # Li_2(1 - 1/sqrt(2))
li2 = mp.polylog(2, arg2)  # Li_2(1 + 1/sqrt(2))

# Compute the difference between the dilogarithms
diff_li = li1 - li2

# Compute the second term: (1/8) * [Li_2(1-1/sqrt(2)) - Li_2(1+1/sqrt(2))]
term2 = (1 / 8) * diff_li

# Sum the two terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))