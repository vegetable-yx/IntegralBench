import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the rational component: 10687/10
rational_part = mp.mpf('10687') / mp.mpf('10')

# Calculate the logarithmic component: 6 * ln(2)
log_part = 6 * mp.log(2)

# Sum the components to get the final result
result = rational_part + log_part

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))