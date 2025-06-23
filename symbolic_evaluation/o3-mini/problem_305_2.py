import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the square root of 5 once for reuse
sqrt5 = mp.sqrt(5)

# Compute the first term: (sqrt(5)/4) * ln((sqrt(5)+1)/(sqrt(5)-1))
log_arg1 = (sqrt5 + 1) / (sqrt5 - 1)
term1 = (sqrt5 / 4) * mp.log(log_arg1)

# Compute the second term: (1/2) * ln((3 - sqrt(5))/2)
log_arg2 = (3 - sqrt5) / 2
term2 = (1/2) * mp.log(log_arg2)

# Third term is ln(2)
term3 = mp.log(2)

# Compute the dilogarithm part: Li_2((1-sqrt5)/2) - Li_2((1+sqrt5)/2)
arg1 = (1 - sqrt5) / 2
arg2 = (1 + sqrt5) / 2
dilog_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)
term4 = - (1/4) * dilog_diff

# Sum all terms
result = term1 + term2 + term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))