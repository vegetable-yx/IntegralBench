import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the first term: pi/(2*sqrt(2))
term1 = mp.pi / (2 * mp.sqrt(2))

# Calculate the argument for the logarithm: (sqrt(2) + 1)/2
log_arg = (mp.sqrt(2) + 1) / 2

# Calculate the second term: (pi/2) * ln((sqrt(2)+1)/2)
term2 = (mp.pi / 2) * mp.log(log_arg)

# Combine the terms: result = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))