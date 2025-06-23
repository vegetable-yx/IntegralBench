import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate each term separately
# First term: π divided by 8
pi_term = mp.pi / 8

# Second term: 3 divided by 4
constant_term = mp.mpf(3) / 4

# Third term: natural logarithm of 2 divided by 2
log_term = mp.log(2) / 2

# Combine terms: π/8 - 3/4 - ln(2)/2
result = pi_term - constant_term - log_term

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))