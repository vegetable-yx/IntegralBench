import mpmath as mp
mp.dps = 15

# Calculate 5/3 ratio
five_thirds = mp.mpf(5)/mp.mpf(3)

# Compute natural logarithm of 5/3
log_term = mp.log(five_thirds)

# Calculate 2/5 fraction
two_fifths = mp.mpf(2)/mp.mpf(5)

# Compute difference between logarithm and fraction
difference = log_term - two_fifths

# Multiply by 1/8 for final result
result = difference * mp.mpf(1)/mp.mpf(8)

print(mp.nstr(result, n=10))