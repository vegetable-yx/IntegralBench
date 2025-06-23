import mpmath as mp
mp.dps = 15

# Compute sqrt(5)
sqrt5 = mp.sqrt(5)

# Calculate the first term (3 - sqrt(5))/2
term1 = (3 - sqrt5) / 2

# Compute the argument for the natural log
log_arg = (sqrt5 - 1) / 2

# Calculate the logarithmic term (1/2)*ln((sqrt5-1)/2)
term2 = 0.5 * mp.log(log_arg)

# Combine terms for final result
result = term1 - term2

print(mp.nstr(result, n=10))