import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute arguments for the dilogarithms
term1 = (1 + sqrt3) / 2
term2 = (1 - sqrt3) / 2

# Evaluate dilogarithms for the two terms
dilog1 = mp.polylog(2, term1)
dilog2 = mp.polylog(2, term2)

# Compute the difference of dilogarithms and multiply by 1/2
dilog_diff = dilog1 - dilog2
dilog_part = 0.5 * dilog_diff

# Calculate argument for the logarithm
log_arg = (sqrt3 + 1) / (sqrt3 - 1)

# Evaluate natural logarithm of the argument
log_term = mp.log(log_arg)

# Compute the pi/4 * log_term term
pi_term = (mp.pi / 4) * log_term

# Sum the two parts to get the final result
result = dilog_part + pi_term

# Print result to 10 decimal places
print(mp.nstr(result, n=10))