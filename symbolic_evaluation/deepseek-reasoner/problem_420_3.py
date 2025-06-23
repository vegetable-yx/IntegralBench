import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute first term: (3 - sqrt(5))/2
term1 = (3 - sqrt5) / 2

# Compute argument for logarithm: (sqrt(5) - 1)/2
log_arg = (sqrt5 - 1) / 2

# Calculate second term: 0.5 * ln((sqrt(5)-1)/2)
term2 = 0.5 * mp.log(log_arg)

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))