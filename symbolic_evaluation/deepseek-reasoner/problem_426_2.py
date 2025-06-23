import mpmath as mp
mp.dps = 15

# Calculate natural logarithm of 3
log_part = mp.log(3)

# Calculate pi/4 term
pi_quarter = mp.pi / 4

# Combine both terms for final result
result = log_part + pi_quarter

print(mp.nstr(result, n=10))