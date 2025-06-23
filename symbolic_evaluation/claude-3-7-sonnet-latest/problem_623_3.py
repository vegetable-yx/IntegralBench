import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π
pi = mp.pi

# Calculate natural logarithms
ln2 = mp.log(2)
ln3 = mp.log(3)

# Compute first term: (π * ln(2)) / 2
term1 = (pi * ln2) / 2

# Compute second term: π * ln(3)
term2 = pi * ln3

# Sum the terms for final result
result = term1 + term2

# Print result to 10 decimal places
print(mp.nstr(result, n=10))