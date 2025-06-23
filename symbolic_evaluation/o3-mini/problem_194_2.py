import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute constants
pi = mp.pi
sqrt3 = mp.sqrt(3)

# Calculate the logarithmic term: ln((√3 + 1)/(√3 - 1))
log_arg = (sqrt3 + 1) / (sqrt3 - 1)
log_term = sqrt3 * mp.log(log_arg)

# Compute the polynomial part: π - 6 + logarithmic term
poly_part = pi - 6 + log_term

# First main term: (π/12) * (π - 6 + log_term)
term1 = (pi / 12) * poly_part

# Compute arguments for dilogarithms
arg1 = (1 - sqrt3) / 2  # 1/2 - √3/2
arg2 = (1 + sqrt3) / 2  # 1/2 + √3/2

# Compute difference of dilogarithms
dilog_diff = mp.polylog(2, arg1) - mp.polylog(2, arg2)

# Second main term: (1/3) * dilog_diff
term2 = (1/3) * dilog_diff

# Sum both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))