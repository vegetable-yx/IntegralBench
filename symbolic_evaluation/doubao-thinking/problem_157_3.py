import mpmath as mp
mp.dps = 15

# Calculate e^(-1/4) using mpmath exponential function
exp_term = mp.exp(-mp.mpf(1)/4)

# Calculate square root of pi using mpmath constant and sqrt
sqrt_pi = mp.sqrt(mp.pi)

# Combine all components: 12 * e^(-1/4) * sqrt(pi)
result = 12 * exp_term * sqrt_pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))