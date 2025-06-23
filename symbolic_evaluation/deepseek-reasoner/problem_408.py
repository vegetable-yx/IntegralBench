import mpmath as mp
mp.dps = 15

# Calculate the fraction 5/3
fraction = mp.mpf(5)/mp.mpf(3)

# Compute natural logarithm of the fraction
log_term = mp.log(fraction)

# Calculate first term: ln(5/3)/8
term1 = log_term / 8

# Calculate second term: 1/20
term2 = mp.mpf(1)/20

# Combine terms for final result
result = term1 - term2

print(mp.nstr(result, n=10))