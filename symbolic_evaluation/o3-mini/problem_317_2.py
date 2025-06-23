import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate the arguments for the dilogarithm functions
# term1 = (1 - 1/sqrt(2)) / 2
term1 = (1 - 1/sqrt2) / 2
# term2 = (1 + 1/sqrt(2)) / 2
term2 = (1 + 1/sqrt2) / 2

# Compute the dilogarithm values for term1 and term2
li1 = mp.polylog(2, term1)
li2 = mp.polylog(2, term2)

# Compute the difference of the dilogarithms multiplied by 2*sqrt(2)
partA = 2 * sqrt2 * (li1 - li2)

# Calculate the argument for the natural logarithm: 3 + 2*sqrt(2)
log_arg = 3 + 2 * sqrt2
# Compute the logarithm terms: ln(3 + 2*sqrt(2)) and ln(2)
log_val = mp.log(log_arg)
ln2 = mp.log(2)

# Compute partB: -sqrt(2) * ln(3 + 2*sqrt(2)) * ln(2)
partB = -sqrt2 * log_val * ln2

# Sum the two parts to get the final result
result = partA + partB

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))