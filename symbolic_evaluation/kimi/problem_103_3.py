import mpmath as mp
mp.dps = 15

# Compute π/12
pi_over_12 = mp.pi / 12

# Calculate tangent of π/12
tan_val = mp.tan(pi_over_12)

# Compute natural logarithm of the tangent value
log_val = mp.log(tan_val)

# Compute π/6
pi_over_6 = mp.pi / 6

# Multiply to get the final result
result = pi_over_6 * log_val

print(mp.nstr(result, n=10))