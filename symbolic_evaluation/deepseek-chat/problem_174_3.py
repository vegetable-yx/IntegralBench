import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant 1/16 as an mpmath floating-point number
x_val = mp.mpf(1) / 16

# Compute the dilogarithm function: Li_2(1/16)
dilog_val = mp.polylog(2, x_val)

# Compute pi constant
pi_val = mp.pi

# Compute the result: (π/4) * Li_2(1/16)
result = (pi_val / 4) * dilog_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))