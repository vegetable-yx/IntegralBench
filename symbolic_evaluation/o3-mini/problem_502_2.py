import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the rational part: 10747 / 10
rational_part = mp.mpf(10747) / mp.mpf(10)

# Calculate the logarithmic part: 6 * ln(2)
log_part = mp.mpf(6) * mp.log(2)

# Sum the two parts
result = rational_part + log_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))