import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the common argument: 1/sqrt(2)
x = mp.one / mp.sqrt(2)

# Calculate the polylogarithm terms
# Li_3 terms
li3_pos = mp.polylog(3, x)
li3_neg = mp.polylog(3, -x)

# Li_2 terms
li2_pos = mp.polylog(2, x)
li2_neg = mp.polylog(2, -x)

# Compute the logarithm argument: (sqrt(2) + 1)/(sqrt(2) - 1)
sqrt2 = mp.sqrt(2)
log_arg = (sqrt2 + 1) / (sqrt2 - 1)
log_val = mp.log(log_arg)

# Calculate the two main terms of the expression
term1 = 0.5 * (li3_pos - li3_neg)
term2 = (1/8) * log_val * (li2_pos - li2_neg)

# Combine terms to get the final result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))