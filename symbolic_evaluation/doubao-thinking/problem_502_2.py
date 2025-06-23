import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the rational number part: 10747/10
rational_part = mp.mpf(10747) / mp.mpf(10)

# Calculate the natural logarithm of 2
ln2 = mp.log(2)

# Multiply ln(2) by 6
log_part = 6 * ln2

# Add the two parts
result = rational_part + log_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))