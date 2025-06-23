import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_val = mp.pi

# Calculate natural logarithm of 2
ln2_val = mp.log(2)

# Compute first term: π/4
term1 = pi_val / 4

# Compute second term: (π * ln(2)) / 2
term2 = (pi_val * ln2_val) / 2

# Combine terms: π/4 - (π*ln2)/2
result = term1 - term2

# Print final result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))