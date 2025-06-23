import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute arguments for the dilogarithm functions
arg1 = (3 - sqrt5) / 2
arg2 = (3 + sqrt5) / 2

# Calculate the two dilogarithm terms
li2_term1 = mp.polylog(2, arg1)
li2_term2 = mp.polylog(2, arg2)

# Compute the difference between the two dilogarithm terms
diff_li2 = li2_term1 - li2_term2

# First term: (1/(2*sqrt5)) * (Li2(arg1) - Li2(arg2))
first_term = diff_li2 / (2 * sqrt5)

# Compute argument for the logarithm: (sqrt5 + 1)/2
log_arg = (sqrt5 + 1) / 2

# Calculate natural logarithm of log_arg
log_val = mp.log(log_arg)

# Second term: (pi/(4*sqrt5)) * ln(log_arg)
second_term = (mp.pi / (4 * sqrt5)) * log_val

# Sum the two terms to get the final result
result = first_term + second_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))