import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute first term: (3 - sqrt(5))/2
term1 = (3 - sqrt5) / 2

# Calculate argument for logarithm: (sqrt(5) - 1)/2
log_argument = (sqrt5 - 1) / 2

# Compute logarithmic term: 0.5 * ln((sqrt(5)-1)/2)
term2 = 0.5 * mp.log(log_argument)

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))