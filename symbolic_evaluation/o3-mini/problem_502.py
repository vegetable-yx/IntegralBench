import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the rational part: 10747 / 10
rational_part = mp.mpf(10747) / 10

# Calculate the logarithmic part: 6 * ln(2)
log_part = 6 * mp.log(2)

# Sum both parts to get the result
result = rational_part + log_part

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))