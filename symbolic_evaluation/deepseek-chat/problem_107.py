import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π²/6: the value of the Riemann zeta function at 2
pi_sq_over_6 = mp.pi**2 / 6

# Compute the dilogarithm Li₂(1/4)
dilog_term = mp.polylog(2, mp.mpf(1)/4)

# Combine the terms: π²/6 - Li₂(1/4)
result = pi_sq_over_6 - dilog_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))